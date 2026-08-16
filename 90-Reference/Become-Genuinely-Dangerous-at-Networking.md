# Become Genuinely Dangerous at Networking

**Question this guide answers:** Are [roadmap.sh Network Engineer](https://roadmap.sh/network-engineer) + [this YouTube playlist](https://www.youtube.com/playlist?list=PLw6kwOJVj3MbMZ8B72ZgUryj8OSETC0ds) enough to become extremely good at network engineering?

**Short answer:** Yes as your **curriculum spine**. No as your **entire training system**.

Use them as the foundation, then add deep-practice layers around them until you can systematically root-cause obscure production failures.

Related local docs: [`Network-Engineer-Roadmap.md`](Network-Engineer-Roadmap.md) · [`roadmap-extracts/`](../roadmap-extracts/) · [`ai/context/03-roadmap-and-curriculum.md`](../ai/context/03-roadmap-and-curriculum.md)

---

## The distinction that matters

There are three different levels:

**1. Know networking**

> “I understand VLANs, OSPF, subnetting, TCP/IP.”

**2. Be a network engineer**

> “I can configure, troubleshoot, monitor and maintain production networks.”

**3. Be extremely good at networking**

> “Give me a broken enterprise network with an obscure routing, MTU, DNS, asymmetric-path, STP, ACL, BGP or TCP problem and I can systematically find the root cause.”

You want **#3**.

That requires much more than watching videos.

---

## Your networking stack

### Layer 1 — Theory

Use the YouTube playlist + [roadmap.sh Network Engineer](https://roadmap.sh/network-engineer).

Deeply understand:

- OSI / TCP-IP
- Ethernet
- ARP
- MAC learning
- Switching
- VLANs
- Trunking
- STP / RSTP / MST
- IPv4 / IPv6
- Subnetting
- Routing
- ICMP
- TCP / UDP
- DNS / DHCP / NAT
- HTTP / HTTPS / TLS
- SSH / SNMP / NTP / Syslog

This is your **foundation**.

A strong academic networking course (e.g. NPTEL Computer Networks) can go deeper into transport protocols, routing, BGP, routers, SDN, Ethernet, ARP/DHCP, wireless, and network security.

---

### Layer 2 — Cisco (CCNA as first hard checkpoint)

Don’t just study the CCNA blueprint. **Build everything.**

Example topology:

```text
PC1 ── SW1 ── SW2 ── Router1 ── Router2 ── Server
       │       │
     VLAN10  VLAN20
```

Implement:

- VLANs
- Trunks
- Inter-VLAN routing
- DHCP
- NAT
- ACLs
- OSPF
- IPv6
- STP
- EtherChannel

Then deliberately **break it**.

That’s where engineering skill starts.

---

### Layer 3 — Packet analysis (non-negotiable)

Learn Wireshark until you can look at a capture and reason:

```text
DNS query
    ↓
TCP SYN
    ↓
SYN/ACK
    ↓
ACK
    ↓
TLS handshake
    ↓
HTTP request
    ↓
HTTP response
```

And identify:

- Retransmissions
- Duplicate ACKs
- Packet loss
- Latency
- TCP window problems
- DNS failures
- MTU problems
- TLS failures
- Asymmetric routing
- Connection resets

[Practical Networking](https://www.practicalnetworking.net/index/networking-fundamentals-how-data-moves-through-the-internet/) is especially useful because it focuses on **how packets actually travel**, not just CLI commands.

---

### Layer 4 — Linux networking

Go beyond a typical CCNA learner. Be comfortable with:

```bash
ip addr
ip route
ip neigh
ip link
ss
tcpdump
ping
traceroute
dig
nslookup
curl
wget
nc
nmap
arp
ethtool
iptables/nftables
```

Understand what the kernel is doing.

Target question:

> What happens inside Linux when you execute `curl https://google.com`?

Eventually walk through the entire process end to end.

---

### Layer 5 — Routing (where you become serious)

#### IGP

- Static routing
- OSPF
- IS-IS

#### EGP

- BGP

Especially BGP. You don’t need to be an ISP engineer immediately, but you should understand:

- AS numbers
- eBGP / iBGP
- Route advertisements
- Route selection
- Local preference
- MED
- AS-path
- Communities
- Route filtering
- Route aggregation
- Route reflectors
- BGP convergence

---

### Layer 6 — Enterprise networking

Build realistic environments. Learn:

- HSRP / VRRP
- Redundancy
- Campus architecture
- Data-center networking
- Spine-leaf
- VXLAN / EVPN
- SD-WAN
- WAN
- MPLS concepts
- QoS
- Multicast
- Wireless
- NAC
- Load balancing

You don’t need expert mastery of all of these immediately. By the time you’re senior, they should not be foreign.

---

### Layer 7 — Security

This is where networking becomes extremely valuable for cybersecurity:

```text
Networking
      ↓
Firewall
      ↓
IDS/IPS
      ↓
VPN
      ↓
NAC
      ↓
Segmentation
      ↓
Zero Trust
      ↓
Cloud Networking
```

Learn:

- Stateful firewalls / NGFW
- ACLs
- IPsec / SSL VPN
- IDS / IPS
- DMZ
- Network segmentation / microsegmentation
- ZTNA
- SASE / SSE
- NAC
- DDoS
- DNS security

Eventually become competent with **Palo Alto + Fortinet**, rather than memorizing ten firewall vendors.

---

### Layer 8 — Automation

Add this heavily to the roadmap.

Learn **Python**, then:

- REST APIs
- JSON / YAML
- Git
- Ansible
- Netmiko
- NAPALM
- Paramiko
- Terraform
- CI/CD concepts

Target capability:

> “I need to change this configuration across 400 devices.”

Write automation instead of SSHing into 400 boxes.

---

### Layer 9 — Cloud networking

You cannot aim for top-tier security architecture while ignoring cloud.

#### AWS

- VPC, subnets, route tables
- IGW, NAT Gateway, Transit Gateway
- Security groups, NACLs
- PrivateLink, VPN, Direct Connect

#### Azure

- VNets, NSGs, Azure Firewall
- VPN Gateway, ExpressRoute
- Private Link, Azure routing

---

### And finally: troubleshooting

This is the **most important missing ingredient**.

You can know 1,000 networking concepts and still be a mediocre engineer. Elite engineers have a **troubleshooting methodology**.

For every failure:

```text
Physical
   ↓
Data Link
   ↓
Network
   ↓
Transport
   ↓
Application
```

Don’t randomly type commands.

1. Form a hypothesis  
2. Test it  
3. Eliminate possibilities  
4. Repeat  

That mentality is the goal.

---

## Is your combination enough?

| Component | Value |
| --- | ---: |
| YouTube playlist | **8/10** foundation |
| roadmap.sh Network Engineer | **8.5/10** curriculum map |
| CCNA | **9/10** structured checkpoint |
| Packet Tracer | **7/10** |
| GNS3 / EVE-NG | **9/10** |
| Wireshark | **10/10** |
| Linux networking | **10/10** |
| Real troubleshooting | **10/10** |
| Real production experience | **10/10** |
| BGP / advanced routing | **9/10** |
| Automation | **9/10** |
| Cloud networking | **10/10** |

### Verdict

- **YouTube + roadmap.sh = YES** for your curriculum spine  
- **YouTube + roadmap.sh = NO** as the entire training system  

---

## The system to follow (every topic)

```text
LEARN
  ↓
CONFIGURE
  ↓
CAPTURE
  ↓
BREAK
  ↓
TROUBLESHOOT
  ↓
AUTOMATE
  ↓
DOCUMENT
```

### Example: OSPF

Don’t do:

> Watch OSPF video → memorize commands → move on.

Do this:

1. **Learn** — What is OSPF? Why does it exist?  
2. **Configure** — Build a 5-router topology  
3. **Capture** — Inspect OSPF packets in Wireshark  
4. **Break** — Kill an interface  
5. **Troubleshoot** — Determine why adjacency disappeared  
6. **Automate** — Configure with Ansible  
7. **Document** — Write a technical incident report explaining exactly what happened  

That’s how you go from **student → engineer**.

---

## Brutal mastery standard

Before you call a topic “mastered,” answer all four:

1. **What is it?** — Theory  
2. **How does it actually work?** — Packet / protocol-level understanding  
3. **How do I configure it?** — CLI / API  
4. **How do I troubleshoot it when it breaks?** — Real engineering  

If you can do all four, **you know it**.  
If you can only answer #1 and #3, you memorized it.

---

## Eventual target

By the time you move seriously into network security, you should look at this:

```text
             INTERNET
                 |
              ISP-A
                 |
              BGP/EDGE
                 |
        +--------+--------+
        |                 |
     FW-A                FW-B
        |                 |
      CORE==============CORE
       /|\               /|\
      / | \             / | \
   VLANs Servers      DMZ  VPN
      |
   Access
   Switches
      |
  Endpoints
```

…and immediately ask:

- Where are the trust boundaries?
- Where are the routing domains?
- Where can asymmetric routing occur?
- Where is NAT occurring?
- Where are the ACLs?
- Where does BGP converge?
- Where is the default route?
- Where is east-west traffic controlled?
- Where are the security telemetry points?
- Where would an attacker move laterally?
- Where would I deploy IDS/IPS?
- Where would I place segmentation?
- What happens if FW-A dies?
- What happens if ISP-A dies?
- How do I prove the failure with packet captures?

**That is the level to reach.**

roadmap.sh + the playlist can absolutely be the **starting spine** for that journey. The mistake would be treating them as the **whole journey**.

---

## Sources

- [roadmap.sh — Network Engineer](https://roadmap.sh/network-engineer)
- [YouTube playlist (spine media)](https://www.youtube.com/playlist?list=PLw6kwOJVj3MbMZ8B72ZgUryj8OSETC0ds)
- [Practical Networking — How data moves through the Internet](https://www.practicalnetworking.net/index/networking-fundamentals-how-data-moves-through-the-internet/)
