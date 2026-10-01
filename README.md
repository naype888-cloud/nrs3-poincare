# NRS³ · Poincaré

**Planck's law forces discrete energy levels** — Poincaré's 1912 theorem in full: any density of
states with Planck's mean energy is `c · ∑ δ_{nε}`. Lean 4.

**[▶ Try it: smear the levels and watch Planck's law break](https://naype888-cloud.github.io/nrs3-poincare/)**

![NRS³ · Poincaré](docs/figures/poincare1912_discreteness.png)

## Results

| Statement | Lean |
|---|---|
| quantized oscillator: mean energy `ε / (e^{βε} − 1)` | `Poincare1911.quantum_mean_energy` |
| continuous oscillator: `1/β`, strictly above Planck | `Poincare1911.planck_lt_rayleigh_jeans` |
| the Laplace transform on `β > 0` determines the weight (possibly of infinite mass) | `Poincare1912.eq_of_laplace` |
| Planck's mean energy at every `β` forces `μ = c · ∑ δ_{nε}`, `c > 0` | `Poincare1912.planck_forces_levels` |
| no density `w(E) dE` reproduces Planck | `Poincare1912.no_density_planck` |

![Poincaré 1911](docs/figures/poincare1911_planck_vs_rj.png)

## In NRS³

NRS works on finite lattices, where the quantum of uncertainty is algebraic. Poincaré is the
historical precedent for discreteness being forced by an exact law rather than assumed; no claim
is made that NRS derives Planck's law.

## History

Poincaré, *Sur la théorie des quanta* (1912), after the first Solvay conference (1911). The
proof here: the mean-energy law makes `Z(β)(1 − e^{−βε})` constant; tilting by `e^{−E}`, analytic
continuation of the complex moment generating function and characteristic functions separate the
weights.

## Build

Lean 4 `v4.34.0`, Mathlib `v4.34.0`, nothing else.

```bash
lake exe cache get
lake build
lake env lean Verification/Axioms.lean   # only propext, Classical.choice, Quot.sound
```

Every file: no `sorry`, lines of at most 100 characters, English headers.

## The mosaic

- [NRS and NRS³ — the base theorem](https://github.com/naype888-cloud/nava-robertson-schrodinger)
- [NRS³ · Cramér–Rao](https://github.com/naype888-cloud/nrs3-cramer-rao)
- [NRS³ · Mandelstam–Tamm](https://github.com/naype888-cloud/nrs3-mandelstam-tamm)
- [NRS³ · Penrose](https://github.com/naype888-cloud/nrs3-penrose)
- [NRS³ · Pauli–Dirac](https://github.com/naype888-cloud/nrs3-pauli-dirac)
- **[NRS³ · Poincaré](https://github.com/naype888-cloud/nrs3-poincare)** (this one)

## License

NRS Noncommercial License 1.0.0, see [`LICENSE`](LICENSE). Author: Eduardo Nava-Hernandez.
