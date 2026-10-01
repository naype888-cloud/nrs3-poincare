"""Figures for Poincaré 1911 and 1912 (numpy, matplotlib).

Writes docs/figures/poincare1911_planck_vs_rj.png and docs/figures/poincare1912_discreteness.png.
Exact (Lean): ε/(e^{βε} − 1) < 1/β (Poincare1911); Planck's law forces c · ∑ δ_{nε}
(Poincare1912). The smeared-level curves use the exact Gaussian formula U = U_Planck − βσ²;
they illustrate the theorem and are not part of the proof.

Run:  python3 docs/simulation/figures_poincare.py
"""

import matplotlib.pyplot as plt
import numpy as np

from style import BLUE, GRID, INK, INK2, MUTED, ORANGE, OUT, SURFACE


def planck(x):
    return x / np.expm1(x)



def fig_poincare1911():
    x = np.linspace(1e-3, 8, 800)
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.6, 4.6), dpi=150)

    ax.axhline(1, color=INK2, lw=1.6, label="classical (continuous):  1/β")
    ax.plot(x, planck(x), color=BLUE, lw=2.2, label="Planck (quantized):  ε/(e^(βε) − 1)")
    ax.fill_between(x, planck(x), 1, color=BLUE, alpha=0.10)
    ax.text(3.6, 0.45, "strict gap for every βε > 0\n(Lean: planck_lt_rayleigh_jeans)",
            color=INK2, fontsize=9.5)
    ax.set_xlabel("βε  =  hν / kT")
    ax.set_ylabel("mean energy  ×  β")
    ax.set_ylim(0, 1.12)
    ax.legend(loc="center right", fontsize=9, bbox_to_anchor=(1.0, 0.75))
    ax.set_title("Mean energy of one oscillator", loc="left", fontsize=11.5)

    bx.plot(x, x ** 2, color=INK2, lw=1.6, label="Rayleigh–Jeans  ∝ x²")
    bx.plot(x, x ** 3 / np.expm1(x), color=BLUE, lw=2.2, label="Planck  ∝ x³/(eˣ − 1)")
    xm = 2.8214393721220787
    bx.plot([xm], [xm ** 3 / np.expm1(xm)], "o", color=ORANGE, mec=SURFACE, mew=1.3, ms=7)
    bx.text(xm + 0.2, xm ** 3 / np.expm1(xm) + 0.12, "Wien peak  x ≈ 2.821", color=INK2,
            fontsize=9.5)
    bx.set_ylim(0, 3.2)
    bx.set_xlabel("x  =  hν / kT")
    bx.set_ylabel("spectral energy density (arb. units)")
    bx.legend(loc="upper right", fontsize=9)
    bx.set_title("The ultraviolet catastrophe is avoided", loc="left", fontsize=11.5)

    fig.suptitle("Poincaré 1911 — the continuum cannot give Planck's law", x=0.01, ha="left",
                 fontsize=13, color=INK)
    fig.tight_layout()
    fig.savefig(OUT / "poincare1911_planck_vs_rj.png", facecolor=SURFACE)
    plt.close(fig)



def smeared_mean(beta, sigma):
    """Mean energy (units of ε) of the levels nε smeared by Gaussians of width σ on ℝ.

    The smearing multiplies Z by e^{β²σ²/2}, so U = U_Planck − βσ² exactly.
    """
    return 1 / np.expm1(beta) - beta * sigma ** 2



def fig_poincare1912():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.6, 4.6), dpi=150,
                                 gridspec_kw={"width_ratios": [1, 1.15]})

    e = np.linspace(0, 5.5, 2000)
    sigmas = [(0.25, ORANGE), (0.08, MUTED)]
    for s, c in sigmas:
        w = sum(np.exp(-0.5 * ((e - n) / s) ** 2) / (s * np.sqrt(2 * np.pi)) for n in range(7))
        ax.plot(e, w * 0.25, color=c, lw=1.5, label=f"smeared levels, σ = {s}ε")
    ns = np.arange(6)
    ax.vlines(ns, 0, 1, color=BLUE, lw=2.6)
    ax.plot(ns, np.ones_like(ns), "^", color=BLUE, ms=8, label="the only solution: c · ∑ δ(E − nε)")
    ax.axhline(0.18, color=INK2, lw=1.2, ls="--", label="continuous density (classical)")
    ax.set_xlabel("energy  E / ε")
    ax.set_ylabel("weight  w(E)  (arb. units)")
    ax.set_ylim(0, 1.55)
    ax.legend(loc="upper center", fontsize=8.8, bbox_to_anchor=(0.5, 1.0), ncol=2,
              framealpha=0.95)
    ax.set_xlim(-0.3, 5.5)
    ax.set_title("Candidate densities of states", loc="left", fontsize=11.5)

    betas = np.geomspace(0.05, 6, 300)
    for s, c in sigmas + [(0.03, BLUE)]:
        rel = np.abs(smeared_mean(betas, s) * np.expm1(betas) - 1)
        bx.plot(betas, rel, color=c, lw=1.8, label=f"σ = {s} ε")
    bx.plot(betas, np.abs(1 / planck(betas) - 1), color=INK2, lw=1.4, ls="--",
            label="continuous (classical)")
    bx.set_xscale("log")
    bx.set_yscale("log")
    bx.set_ylim(1e-6, 1e2)
    bx.set_xlabel("βε")
    bx.set_ylabel("|U / U_Planck − 1|")
    bx.text(0.36, 0.04, "smeared levels:  U = U_Planck − βσ²  (exact)\nevery σ > 0 misses Planck; "
            "only σ = 0 reproduces it\n(Lean: planck_forces_levels)", transform=bx.transAxes,
            color=INK2, fontsize=9.5)
    bx.legend(loc="upper left", fontsize=9)
    bx.set_title("Deviation from Planck's mean energy", loc="left", fontsize=11.5)

    fig.suptitle("Poincaré 1912 — Planck's law forces discrete levels", x=0.01, ha="left",
                 fontsize=13, color=INK)
    fig.tight_layout()
    fig.savefig(OUT / "poincare1912_discreteness.png", facecolor=SURFACE)
    plt.close(fig)


if __name__ == "__main__":
    fig_poincare1911()
    fig_poincare1912()
