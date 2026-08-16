---
tags: [linux, networking, ccna, shell, tooling]
aliases: [Bash Networking Toolkit, Linux CLI for Networking, Shell Scripting for Networks]
layer: Operations / host tooling
---

# Shell and Scripting

## Learning objectives

- Use `ip`, `ss`, `ping`, `traceroute`, and `tcpdump` as a daily network engineer toolkit
- Prefer modern commands (`ip` / `ss`) while still reading legacy `ifconfig` / `netstat` output
- Capture and filter packets on the wire for reachability and protocol proof
- Write small bash loops for inventory, ping sweeps, and interface dumps
- Relate host tooling to [[IP Address]], [[ARP]], [[Packet]], and [[Routers]] concepts

## One-sentence definition

> The **shell networking toolkit** is the set of Linux/macOS CLI commands and short scripts that let you inspect interfaces, routes, sockets, and packets — the same mental model as Cisco `show` / `debug`, but on the host.

## Analogy

> Your network is a **city**. The shell is a **street inspector’s radio and clipboard**: `ip` tells you which roads exist and which signs are posted, `ss` lists which doors are open, `ping`/`traceroute` walk the path, and `tcpdump` is a **bodycam** recording every car that passes an intersection.

## Why it matters

CCNA labs live on routers and switches, but real jobs live on **hosts + automation**. Vendors differ; `ip`/`ss`/`tcpdump` do not. If you can prove Layer‑3 reachability, see listening ports, and capture a handshake, you can debug half of “the network is down” tickets without touching the core.

## Deep dive

### Mental model

```text
Host OS
  ├─ Interfaces / addresses     → ip addr, ip link
  ├─ Routes / neighbors         → ip route, ip neigh
  ├─ Sockets (who talks)        → ss -tulpn
  ├─ Path tests                 → ping, traceroute
  ├─ Packets on the wire        → tcpdump / Wireshark
  └─ Config managers (Linux)    → nmcli, systemd-networkd
```

### Mechanism — core commands

| Job | Prefer | Legacy / notes |
|-----|--------|----------------|
| Addresses & links | `ip addr`, `ip link` | `ifconfig` (macOS still common) |
| Routes | `ip route` | `route -n`, `netstat -rn` |
| Neighbors ([[ARP]]) | `ip neigh` | `arp -a` |
| Sockets | `ss -tulpn` | `netstat -tulpn` |
| DNS quick check | `dig`, `getent hosts` | `nslookup` |
| Capture | `tcpdump -ni eth0` | Wireshark GUI |
| Wi‑Fi / NM | `nmcli` | distro‑specific |

**Ping vs traceroute:** `ping` proves *end reachability + RTT*; `traceroute` / `traceroute -n` maps *which hop fails*. Neither replaces a capture when ACLs rewrite or drop silently.

**tcpdump filters (start here):**

```bash
tcpdump -ni any icmp
tcpdump -ni eth0 host 8.8.8.8
tcpdump -ni eth0 port 53
tcpdump -ni eth0 'tcp[tcpflags] & (tcp-syn) != 0'
```

### Scripting loops for inventory

Small scripts beat memory. Pattern: **discover → test → report**.

```bash
#!/usr/bin/env bash
# inventory-ping.sh — ping a CIDR host range (lab use)
NET=192.168.1
for i in $(seq 1 10); do
  ip="$NET.$i"
  if ping -c1 -W1 "$ip" &>/dev/null; then
    echo "UP   $ip"
  else
    echo "DOWN $ip"
  fi
done
```

```bash
#!/usr/bin/env bash
# dump-ifaces.sh — quick interface snapshot
echo "=== addresses ==="
ip -br addr
echo "=== routes ==="
ip route
echo "=== listening ==="
ss -tulpn
```

On macOS, swap `ip` for `ifconfig` / `netstat -rn` / `arp -a` where needed.

### On the wire / fields

When you run `tcpdump`, you are looking at [[Frame]]s: Ethernet header (MACs) → IP header ([[IP Address]]) → TCP/UDP ports → payload. Filters select by those fields. `ss` reads the **kernel socket table**, not the wire — a closed socket won’t show even if old packets exist in a pcap.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| OSI / TCP-IP | L1–L2 | `ip link`, carrier, MAC, ARP neigh |
| OSI / TCP-IP | L3 | `ip addr`, `ip route`, ping, traceroute |
| OSI / TCP-IP | L4 | `ss` ports, tcpdump port filters |
| Operations | Host | Scripts automate discovery & proof |

## Lab exercises

### Lab 1 — Baseline your machine

```bash
# Linux
ip -br link
ip -br addr
ip route
ip neigh
ss -tulpn

# macOS equivalents
ifconfig
netstat -rn
arp -a
netstat -an | head
```

Write down: management IP, default gateway, DNS, and one listening service.

### Lab 2 — Prove a path with capture

```bash
# Terminal A (may need sudo)
sudo tcpdump -ni any icmp

# Terminal B
ping -c 4 1.1.1.1
traceroute -n 1.1.1.1
```

Confirm echo request/reply in the capture. Then filter DNS:

```bash
sudo tcpdump -ni any port 53
dig example.com +short
```

### Optional Cisco parallel

On IOS, map the same jobs: `show ip interface brief`, `show ip route`, `show ip arp`, `show tcp brief`, `ping`, `traceroute`, `debug ip packet` (lab only).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| ping fails, browser “works” | ICMP blocked | tcpdump on TCP/443; try curl |
| No default route | DHCP/static misconfig | `ip route`; gateway ARP (`ip neigh`) |
| Port “should listen” but closed | Bind/firewall | `ss -tulpn`; local firewall |
| tcpdump empty | Wrong iface / filter | `-i any`; loosen filter |
| Script false DOWN | Timeout too aggressive | raise `-W`; check rate limits |

## Common traps / interview gotchas

- `ifconfig` “UP” ≠ you have a useful [[IP Address]] or default route.
- `ping` success ≠ application path (DNS, TLS, proxy, wrong VIP).
- `netstat`/`ss` without process context (`-p`) wastes time on busy hosts.
- Capturing on the wrong VLAN/interface is the #1 false negative.
- Running destructive sweeps on production without approval is a career event — lab ranges only.

## Mastery checklist

- [ ] Replace `ifconfig`/`netstat` habits with `ip`/`ss` on Linux
- [ ] Draw which tool maps to L2 vs L3 vs L4
- [ ] Capture ICMP and DNS with intentional filters
- [ ] Write a 10‑line bash loop that inventories hosts or interfaces
- [ ] Map each host command to a Cisco `show` equivalent

## Related notes

- [[Linux-Roadmap]] · [[IP Address]] · [[ARP]] · [[MAC Address]] · [[Packet]] · [[Frame]] · [[TCP]] · [[UDP]] · [[DNS]] · [[DHCP]]
- ← [[01-Linux-for-Networking/Index|Linux for Networking]] · [[04-Building-a-Network/Index|Building a Network]]
