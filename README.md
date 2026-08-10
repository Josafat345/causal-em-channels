# Canales electromagneticos causales espacio-temporales

Base computacional para estudiar la capacidad fisica de canales gobernados por
Maxwell en medios dispersivos y variables en el tiempo.

## Primer hito

El modelo inicial es un oscilador de Lorentz adimensional con frecuencia de
resonancia modulada periódicamente:

$$
p''(\tau)+2\zeta p'(\tau)
+\left[1+m\cos(\nu\tau+\phi)\right]p(\tau)=f(\tau).
$$

Aquí, $\tau=\omega_0t$, $\zeta=\gamma/(2\omega_0)$,
$m$ es la profundidad de modulación y $\nu=\Omega_m/\omega_0$.
El primer experimento calcula la matriz monodrómica $M$, los multiplicadores de
Floquet $\lambda_i$, las tasas de crecimiento $g_i$ y el balance de energía.

## Instalacion

En PowerShell:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev,notebook]"
python -m ipykernel install --prefix .venv --name causal-em --display-name "Python (causal-em)"
```

La dependencia de optimizacion para etapas posteriores se instala con:

```powershell
python -m pip install -e ".[optimization]"
```

## Ejecucion

```powershell
pytest
causal-em-first --with-map
jupyter lab
```

El comando `causal-em-first` guarda figuras y un resumen JSON en
`results/first_experiment/`. El cuaderno inicial esta en
`notebooks/01_lorentz_floquet.ipynb`.

## Criterios de validez

- La matriz numerica debe coincidir con la exponencial matricial en el caso sin
  modulación.
- El determinante de la monodromia debe satisfacer la identidad de Liouville
  $\det M=\exp(-2\zeta T)$.
- El balance numerico de energia debe reproducir exactamente los terminos de
  disipación y trabajo de modulación al refinar la malla temporal.
- El límite $m\to0$ debe recuperar el oscilador de Lorentz estacionario.
- El núcleo causal debe anularse para $\tau\le s$, obedecer la composición
  del propagador y satisfacer $g(\tau+T,s+T)=g(\tau,s)$.

La derivacion y el alcance de este primer modelo se documentan en
`docs/01_modelo_lorentz_floquet.md`.
