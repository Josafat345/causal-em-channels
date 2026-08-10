# Modelo 01: oscilador de Lorentz periódico

## 1. Propósito

Antes de resolver Maxwell en una geometría espacial, aislamos la dinámica
material responsable de la dispersión, la memoria y la conversión de
frecuencias. Esto permite verificar causalidad, estabilidad y contabilidad de
energía en un sistema pequeño con referencias analíticas exactas.

## 2. Ecuación dimensional

Consideramos una polarización escalar $P(t)$:

$$
\ddot P+\gamma\dot P
+\omega_0^2\left[1+m\cos(\Omega_m t+\phi)\right]P
=\varepsilon_0\omega_p^2 E(t).
$$

La modulación actúa sobre la frecuencia de resonancia. Su mecanismo físico
microscópico y su costo energético se incorporarán explícitamente en una etapa
posterior; por ahora, el término temporal se trata como un bombeo determinista
conocido.

## 3. Forma adimensional

Usando

$$
\tau=\omega_0t,\qquad
\zeta=\frac{\gamma}{2\omega_0},\qquad
\nu=\frac{\Omega_m}{\omega_0},
$$

y absorbiendo la escala del forzamiento en $f(\tau)$, obtenemos

$$
p''+2\zeta p'+k(\tau)p=f(\tau),
\qquad
k(\tau)=1+m\cos(\nu\tau+\phi).
$$

En el primer hito imponemos $|m|<1$, de modo que $k(\tau)>0$. Esto no es una
necesidad matemática general, sino una restricción física conservadora para el
prototipo.

## 4. Sistema de estado y causalidad

Con

$$
\mathbf{x}(\tau)=
\begin{pmatrix}p(\tau)\\v(\tau)\end{pmatrix},
\qquad v(\tau)=p'(\tau),
$$

la ecuación de estado es

$$
\mathbf{x}'=A(\tau)\mathbf{x}+\mathbf{b}f(\tau),\qquad
A(\tau)=
\begin{pmatrix}
0&1\\
-k(\tau)&-2\zeta
\end{pmatrix},\qquad
\mathbf{b}=\begin{pmatrix}0\\1\end{pmatrix}.
$$

La matriz fundamental satisface

$$
\Phi'(\tau)=A(\tau)\Phi(\tau),\qquad \Phi(0)=I_2.
$$

El propagador causal es

$$
U(\tau,s)=\Phi(\tau)\Phi(s)^{-1},\qquad \tau\ge s,
$$

y la respuesta forzada es

$$
\mathbf{x}(\tau)=U(\tau,0)\mathbf{x}(0)
+\int_0^\tau U(\tau,s)\mathbf{b}f(s)\,ds.
$$

La susceptibilidad material causal normalizada que lleva el forzamiento a la
polarización es el núcleo de dos tiempos

$$
g(\tau,s)=\mathbf e_p^{\mathsf T}U(\tau,s)\mathbf b\,H(\tau-s),
\qquad
\mathbf e_p=\begin{pmatrix}1\\0\end{pmatrix}.
$$

No depende solo del retardo $\tau-s$: el medio recuerda también la fase de la
modulación en el instante $s$. Como $A(\tau+T)=A(\tau)$, satisface la periodicidad
conjunta

$$
g(\tau+T,s+T)=g(\tau,s).
$$

Esta es la primera estructura genuinamente espacio-temporal del proyecto. En
el límite estacionario $m=0$, vuelve a depender únicamente de $\tau-s$.

## 5. Teoría de Floquet

El periodo adimensional es

$$
T=\frac{2\pi}{\nu}.
$$

La matriz monodrómica es $M=\Phi(T)$. Sus autovalores $\lambda_i$ son los
multiplicadores de Floquet. La tasa exponencial real asociada es

$$
g_i=\frac{\log|\lambda_i|}{T}.
$$

El sistema homogéneo es asintóticamente estable cuando $|\lambda_i|<1$ para
todo $i$. Los exponentes complejos obtenidos con el logaritmo principal solo
están definidos módulo $2\pi\mathrm{i}/T$; por eso la estabilidad se evalúa con
los módulos, no con una elección arbitraria de rama.

## 6. Identidad exacta de Liouville

Como $\operatorname{tr}A(\tau)=-2\zeta$,

$$
\det M
=\exp\left(\int_0^T\operatorname{tr}A(s)\,ds\right)
=\exp(-2\zeta T).
$$

Esta identidad es una prueba especialmente sensible de la integración
numérica. En ausencia de amortiguamiento, $\det M=1$.

## 7. Balance de energía

Definimos la energía instantánea adimensional

$$
\mathcal{E}(\tau)=\frac12v^2+\frac12k(\tau)p^2.
$$

Entonces

$$
\frac{d\mathcal{E}}{d\tau}
=-2\zeta v^2
+\frac12k'(\tau)p^2
+v f(\tau),
$$

donde

$$
k'(\tau)=-m\nu\sin(\nu\tau+\phi).
$$

Los tres términos son, respectivamente, disipación, trabajo del bombeo de
modulación y potencia de la señal aplicada. El modelo no debe interpretar el
segundo término como ganancia gratuita.

## 8. Limites de este hito

Este sistema aun no incluye propagacion espacial, ruido termico, aperturas,
condiciones de frontera ni capacidad de Shannon. Su funcion es producir una
base validada sobre la cual agregar, en orden:

1. excitacion y observacion lineales;
2. ruido ciclostacionario fisicamente consistente;
3. canal de Floquet y optimizacion de covarianza;
4. una linea de transmision o slab unidimensional;
5. operadores electromagneticos espaciales.
