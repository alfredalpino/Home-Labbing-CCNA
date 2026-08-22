(function () {
  const root = document.documentElement;

  function systemTheme() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function resolveTheme() {
    const saved = localStorage.getItem("theme");
    if (saved === "light" || saved === "dark") return saved;
    return systemTheme();
  }

  function commitTheme(next) {
    root.setAttribute("data-theme", next);
    localStorage.setItem("theme", next);
    const btn = document.getElementById("theme-toggle");
    if (btn) {
      const isDark = next === "dark";
      btn.textContent = isDark ? "Light" : "Dark";
      btn.setAttribute(
        "aria-label",
        isDark ? "Switch to light mode" : "Switch to dark mode"
      );
      btn.title = isDark ? "Light mode" : "Dark mode";
    }
  }

  async function toggleTheme() {
    const current = root.getAttribute("data-theme") || resolveTheme();
    const next = current === "dark" ? "light" : "dark";
    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduced) {
      commitTheme(next);
      return;
    }
    root.classList.add("theme-fading");
    try {
      await root.animate([{ opacity: 1 }, { opacity: 0 }], {
        duration: 140,
        easing: "ease-out",
        fill: "forwards",
      }).finished;
      commitTheme(next);
      await root.animate([{ opacity: 0 }, { opacity: 1 }], {
        duration: 180,
        easing: "ease-in",
        fill: "forwards",
      }).finished;
    } catch {
      commitTheme(next);
    } finally {
      root.style.opacity = "";
      root.classList.remove("theme-fading");
    }
  }

  commitTheme(resolveTheme());

  document.getElementById("theme-toggle")?.addEventListener("click", toggleTheme);

  const menuBtn = document.getElementById("menu-toggle");
  const backdrop = document.getElementById("nav-backdrop");
  function closeNav() {
    document.body.classList.remove("nav-open");
  }
  menuBtn?.addEventListener("click", () => {
    document.body.classList.toggle("nav-open");
  });
  backdrop?.addEventListener("click", closeNav);
  document.querySelectorAll(".sidebar a").forEach((a) => {
    a.addEventListener("click", closeNav);
  });

  const search = document.getElementById("note-search");
  const items = Array.from(document.querySelectorAll("[data-nav-item]"));
  search?.addEventListener("input", () => {
    const q = search.value.trim().toLowerCase();
    items.forEach((el) => {
      const hay = (el.getAttribute("data-nav-item") || "").toLowerCase();
      el.style.display = !q || hay.includes(q) ? "" : "none";
    });
    document.querySelectorAll(".nav-section").forEach((sec) => {
      const visible = Array.from(sec.querySelectorAll("[data-nav-item]")).some(
        (el) => el.style.display !== "none"
      );
      sec.style.display = visible ? "" : "none";
      if (q && visible) sec.open = true;
    });
  });

  window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", () => {
      const saved = localStorage.getItem("theme");
      if (saved !== "light" && saved !== "dark") commitTheme(systemTheme());
    });
})();
