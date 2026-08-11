# Resultado 01: resonancia paramétrica y núcleo causal

## Configuración

El experimento reproducible usa

```math
\zeta=0.02,\qquad m=0.20,\qquad \nu=2,\qquad T=\pi.
```

Es el centro esperado de la primera lengua de inestabilidad del oscilador de
Mathieu amortiguado. Por tanto, este caso es deliberadamente un benchmark y no
una afirmación de novedad.

## Resultado de Floquet

La integración produce

```math
M\approx
\begin{pmatrix}
-0.9477618712 & 0.1462576703\\
 0.1496392219 &-0.9536121780
\end{pmatrix},
```

con multiplicadores

```math
\lambda_1\approx-1.0986547255,
\qquad
\lambda_2\approx-0.8027193238.
```

Como el radio espectral satisface $\rho(M)=1.0986547>1$, existe amplificación
paramétrica y la tasa máxima de crecimiento es

```math
g_{\max}\approx0.02994865
```

por unidad de tiempo adimensional. A la vez,

```math
\det M_{\mathrm{num}}=0.8819113782980792,
\qquad
e^{-2\zeta T}=0.8819113782981763,
```

con error absoluto menor que $10^{-13}$. Este ejemplo muestra algo físicamente
importante: $\det M<1$ no implica estabilidad. La disipación contrae el área de
fase, mientras el bombeo puede expandir una dirección y contraer la otra.

## Contabilidad de energía

El residuo normalizado de

```math
\mathcal{E}(\tau)-\mathcal{E}(0)
=W_{\mathrm{dis}}(\tau)+W_{\mathrm{mod}}(\tau)+W_{\mathrm{in}}(\tau)
```

es $3.6\times10^{-10}$. El crecimiento observado proviene del trabajo de modulación, no
de una ganancia gratuita agregada al canal.

## Núcleo causal de dos tiempos

El código calcula

```math
g(\tau,s)=\mathbf e_p^{\mathsf T}U(\tau,s)\mathbf b\,H(\tau-s).
```

Se verifica numéricamente:

- causalidad estricta para $\tau\le s$;
- composición $U(\tau,s)=U(\tau,u)U(u,s)$;
- periodicidad conjunta $g(\tau+T,s+T)=g(\tau,s)$;
- recuperación de la función de Green exacta cuando $m=0$.

## Lectura científica

El diagrama reproduce la lengua principal alrededor de $\nu=2$ y una lengua
secundaria alrededor de $\nu=1$ para modulaciones más intensas. Esto valida la
base numérica frente a fenómenos conocidos. La novedad potencial empezará al
conectar este núcleo causal con ruido físicamente consistente, observación de
puertos y una restricción conjunta de energía de señal y bombeo.

Como contrapunto apto para el futuro canal de horizonte largo, el benchmark
$\nu=3$ produce un par conjugado con

```math
|\lambda_1|=|\lambda_2|\approx0.958977274,
\qquad g_{\max}\approx-0.02.
```

Este régimen es asintóticamente estable y será la configuración base del
siguiente hito. El caso $\nu=2$ se conserva como prueba de que el método detecta
correctamente una región que debe excluirse o regularizarse.

El siguiente resultado falsable será comparar dos representaciones del mismo
canal estable:

1. convolución causal de dos tiempos en el dominio temporal;
2. matriz de transferencia armónica truncada en bandas laterales de Floquet.

Ambas deben predecir la misma respuesta y converger al aumentar el número de
armónicos. Solo después conviene formular capacidad y optimización de
covarianza.
