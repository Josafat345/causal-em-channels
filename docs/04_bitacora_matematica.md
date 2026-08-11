# Bitácora matemática de investigación

> **Proyecto:** teoría causal de canales electromagnéticos espacio-temporales
>
> **Inicio formal de la bitácora:** 11 de agosto de 2026
>
> **Última actualización:** 11 de agosto de 2026
>
> **Hito activo:** equivalencia entre el núcleo causal y la representación armónica
> de Floquet
>
> **Regla de escritura:** toda ecuación, aproximación, hipótesis y prueba numérica
> debe quedar registrada antes de aceptarse como parte del modelo.

## 0. Cómo se usará este cuaderno

Este archivo no sustituye al marco teórico. Su función es conservar los cálculos
como si fueran resoluciones hechas a mano. Cada hoja responde siempre a cinco
preguntas:

1. ¿Qué datos y convenciones estamos usando?
2. ¿Qué queremos calcular o demostrar?
3. ¿Cómo se obtiene el resultado, sin saltar pasos?
4. ¿Cómo verificamos signos, unidades y límites?
5. ¿Qué queda pendiente?

Usaremos un estado principal cerrado y, cuando haga falta, una nota de alcance:

- **[DERIVADO]:** el procedimiento algebraico está escrito.
- **[VERIFICADO]:** existe además una prueba analítica independiente o una prueba
  numérica automatizada.
- **[HIPÓTESIS]:** es una afirmación que todavía debe probarse o refutarse.
- **[PENDIENTE]:** aún no se ha realizado el cálculo.
- **[CORREGIDO]:** se conserva constancia de una modificación posterior.

Palabras como *implementado*, *contrastado numéricamente* o *dimensión finita*
describen la evidencia o el alcance; no crean estados adicionales.

Las hojas no se borrarán cuando cambie el modelo. Si encontramos un error, se
añadirá una nota de corrección indicando qué cambió y por qué.

## 1. Índice de hojas

| Hoja | Cálculo | Estado al 11-08-2026 |
|---|---|---|
| M-000 | Convenciones y notación de trabajo | [VERIFICADO] |
| M-001 | Adimensionalización del oscilador de Lorentz | [DERIVADO]; ecuación implementada |
| M-002 | Forma de estado y fórmula de Duhamel | [DERIVADO]; composición verificada |
| M-003 | Salto impulsivo y núcleo causal de dos tiempos | [DERIVADO]; causalidad y periodicidad verificadas |
| M-004 | Función de Green exacta para $m=0$ | [VERIFICADO] numéricamente |
| M-005 | Monodromía, multiplicadores y estabilidad | [VERIFICADO] |
| M-006 | Identidad de Liouville | [VERIFICADO] |
| M-007 | Balance exacto de energía | [VERIFICADO] |
| M-008 | Umbral aproximado de la primera lengua de Mathieu | [DERIVADO]; contrastado numéricamente |
| M-009 | Benchmarks inestable y estable | [VERIFICADO] numéricamente |
| M-010 | Cota exponencial del propagador estable | [VERIFICADO] en dimensión finita |
| M-011 | Balance armónico del Lorentz modulado | [DERIVADO]; implementación pendiente |
| M-012 | Truncamiento y matriz de transferencia de Floquet | [DERIVADO]; implementación pendiente |
| M-013 | Puente causal–Floquet y protocolo de equivalencia | [DERIVADO] formal; experimento [PENDIENTE] |

### Registro cronológico

| Fecha | Registro | Decisión o resultado |
|---|---|---|
| 10-08-2026 | Hito numérico inicial | Se validaron monodromía, Liouville, energía y núcleo causal en casos estable e inestable. |
| 10-08-2026 | Marco teórico | Se fijó el programa Maxwell–Lorentz, Floquet, ruido y capacidad. |
| 11-08-2026 | Inicio formal de la bitácora | Se reconstruyeron como cálculos las hojas M-000 a M-010. |
| 11-08-2026 | Hito activo | Se derivaron las hojas M-011 a M-013; la implementación armónica sigue pendiente. |
| 11-08-2026 | Auditoría matemática inicial | Se corrigieron el alcance del centro resonante, el signo temporal del trabajo neto y el protocolo de convergencia. |
| 11-08-2026 | Corrección de renderizado GFM | Se migraron las ecuaciones de bloque a fences `math` y se protegieron los escapes sensibles de expresiones inline. |

Cada sesión futura añadirá una fila sin reemplazar las anteriores.

### Mapa de evidencia

| Hojas | Implementación o prueba relacionada |
|---|---|
| M-001 y M-007 | [`src/causal_em/lorentz.py`](../src/causal_em/lorentz.py) y [`tests/test_lorentz.py`](../tests/test_lorentz.py) |
| M-002 a M-004 | [`src/causal_em/causal.py`](../src/causal_em/causal.py) y [`tests/test_causal.py`](../tests/test_causal.py) |
| M-005, M-006 y M-008 | [`src/causal_em/floquet.py`](../src/causal_em/floquet.py) y [`tests/test_floquet.py`](../tests/test_floquet.py) |
| M-009 | [`src/causal_em/experiments/first_experiment.py`](../src/causal_em/experiments/first_experiment.py) |
| M-010 | Demostración finito-dimensional registrada; generalización espacial pendiente. |
| M-011 a M-013 | Derivación registrada; todavía no existe implementación que pueda contarse como verificación. |

---

## Hoja M-000 — Convenciones y notación de trabajo

**Fecha:** 11-08-2026

**Estado:** [VERIFICADO]

### Datos

La convención de Fourier del proyecto es

```math
\widehat f(\omega)
=\int_{-\infty}^{\infty}
f(t)e^{\mathrm{i}\omega t}\,dt,
```

```math
f(t)
=\frac{1}{2\pi}
\int_{-\infty}^{\infty}
\widehat f(\omega)e^{-\mathrm{i}\omega t}\,d\omega.
```

Por tanto, una componente de frecuencia positiva se escribe

```math
f(t)=F e^{-\mathrm{i}\omega t}.
```

### Consecuencias que debemos recordar

Al derivar una componente armónica,

```math
\frac{d}{dt}e^{-\mathrm{i}\omega t}
=-\mathrm{i}\omega e^{-\mathrm{i}\omega t},
```

```math
\frac{d^2}{dt^2}e^{-\mathrm{i}\omega t}
=-\omega^2e^{-\mathrm{i}\omega t}.
```

Con esta convención, la transformada de una respuesta causal BIBO estable cuyo
núcleo temporal pertenece a $L^1(0,\infty)$ admite una prolongación analítica para

```math
\mathrm{Im}\,\omega>0,
```

y los polos de un sistema racional exponencialmente estable quedan en

```math
\mathrm{Im}\,\omega_p<0.
```

### Notación temporal

Usaremos

```math
\tau=\omega_0t
```

para el tiempo adimensional. El periodo de modulación en esa variable será

```math
T_m=\frac{2\pi}{\Omega_m}
```

en tiempo físico y

```math
T_\tau=\frac{2\pi}{\nu}.
```

En documentos anteriores se escribió simplemente $T$. Dentro de esta bitácora se
usará $T_\tau$ para evitar confundirlo con temperatura o con un periodo dimensional.

### Comprobación rápida

Como

```math
\nu=\frac{\Omega_m}{\omega_0},
```

entonces

```math
T_\tau
=\omega_0\frac{2\pi}{\Omega_m}
=\frac{2\pi}{\nu},
```

que es adimensional, como debe ser.

### Resultado de la hoja

```math
\boxed{
e^{-\mathrm{i}\omega t},
\qquad
\tau=\omega_0t,
\qquad
T_\tau=\frac{2\pi}{\nu}
}
```

Todas las fases del balance armónico se comprobarán contra estas convenciones.

---

## Hoja M-001 — Adimensionalización del oscilador de Lorentz

**Fecha:** 11-08-2026

**Estado:** [DERIVADO]; ecuación implementada en `src/causal_em/lorentz.py`

### Problema

Partimos del modelo dimensional

```math
\ddot P(t)
+\gamma\dot P(t)
+\omega_0^2
\left[1+m\cos(\Omega_mt+\phi)\right]P(t)
=\varepsilon_0\omega_p^2E(t).
```

Queremos escribirlo en variables adimensionales sin perder ningún factor de
$\omega_0$.

### Paso 1 — Escalas

Definimos

```math
\tau=\omega_0t,
\qquad
P(t)=P_\star p(\tau),
```

donde $P_\star$ es una escala de polarización todavía arbitraria.

Por la regla de la cadena,

```math
\dot P(t)
=P_\star\frac{dp}{d\tau}\frac{d\tau}{dt}
=P_\star\omega_0p'(\tau),
```

y

```math
\ddot P(t)
=P_\star\omega_0^2p''(\tau).
```

La fase de modulación cambia como

```math
\Omega_mt+\phi
=\frac{\Omega_m}{\omega_0}\tau+\phi.
```

### Paso 2 — Sustitución

Sustituyendo las derivadas,

```math
P_\star\omega_0^2p''
+\gamma P_\star\omega_0p'
+\omega_0^2
\left[1+m\cos\left(
\frac{\Omega_m}{\omega_0}\tau+\phi
\right)\right]
P_\star p
=\varepsilon_0\omega_p^2E\left(\frac{\tau}{\omega_0}\right).
```

Dividimos toda la ecuación por $P_\star\omega_0^2$:

```math
p''
+\frac{\gamma}{\omega_0}p'
+\left[1+m\cos\left(
\frac{\Omega_m}{\omega_0}\tau+\phi
\right)\right]p
=\frac{\varepsilon_0\omega_p^2}
{P_\star\omega_0^2}
E\left(\frac{\tau}{\omega_0}\right).
```

### Paso 3 — Parámetros finales

Definimos

```math
\zeta=\frac{\gamma}{2\omega_0},
\qquad
\nu=\frac{\Omega_m}{\omega_0},
```

```math
f(\tau)
=\frac{\varepsilon_0\omega_p^2}
{P_\star\omega_0^2}
E\left(\frac{\tau}{\omega_0}\right),
```

Si elegimos una escala de campo $E_\star$ y tomamos

```math
P_\star
=\frac{\varepsilon_0\omega_p^2}{\omega_0^2}E_\star,
```

entonces el forzamiento se simplifica a

```math
f(\tau)=\frac{E(\tau/\omega_0)}{E_\star}.
```

Definimos además

```math
k(\tau)=1+m\cos(\nu\tau+\phi).
```

Obtenemos finalmente

```math
\boxed{
p''(\tau)+2\zeta p'(\tau)+k(\tau)p(\tau)=f(\tau)
}.
```

### Comprobaciones

1. Cada término de la ecuación final es adimensional.
2. Si $m=0$, recuperamos el oscilador de Lorentz estacionario normalizado.
3. Si $|m|<1$, entonces

   ```math
   k(\tau)\ge 1-|m|>0.
   ```

4. La derivada de la rigidez es

   ```math
   k'(\tau)
   =-m\nu\sin(\nu\tau+\phi).
   ```

Esta última expresión se usará en el balance de energía.

---

## Hoja M-002 — Forma de estado y fórmula de Duhamel

**Fecha:** 11-08-2026

**Estado:** [DERIVADO]; composición del propagador verificada numéricamente

### Problema

Convertir

```math
p''+2\zeta p'+k(\tau)p=f(\tau)
```

en un sistema de primer orden y obtener su solución forzada.

### Paso 1 — Variables de estado

Tomamos

```math
v(\tau)=p'(\tau),
\qquad
\mathbf x(\tau)
=\begin{pmatrix}
p(\tau)\\
v(\tau)
\end{pmatrix}.
```

Entonces

```math
p'=v,
```

```math
v'=-k(\tau)p-2\zeta v+f(\tau).
```

En forma matricial,

```math
\boxed{
\mathbf x'(\tau)
=\mathbf A(\tau)\mathbf x(\tau)
+\mathbf b f(\tau)
},
```

con

```math
\mathbf A(\tau)
=\begin{pmatrix}
0&1\\
-k(\tau)&-2\zeta
\end{pmatrix},
\qquad
\mathbf b
=\begin{pmatrix}
0\\
1
\end{pmatrix}.
```

### Paso 2 — Propagador homogéneo

Definimos $\mathbf U(\tau,s)$ mediante

```math
\frac{\partial}{\partial\tau}\mathbf U(\tau,s)
=\mathbf A(\tau)\mathbf U(\tau,s),
\qquad
\mathbf U(s,s)=\mathbf I.
```

La propiedad de composición debe ser

```math
\boxed{
\mathbf U(\tau,u)\mathbf U(u,s)=\mathbf U(\tau,s)
},
\qquad
\tau\ge u\ge s.
```

El propagador es invertible. Extendemos su definición a tiempos en cualquier orden
mediante

```math
\boxed{
\mathbf U(\tau,s)
=\mathbf U(s,\tau)^{-1}
},
\qquad
\tau<s.
```

Con esta extensión, la ley de composición sigue siendo válida siempre que todos
los propagadores estén definidos; el orden escrito arriba solo facilita su lectura
como evolución hacia adelante.

### Paso 3 — Variación de constantes

Multiplicamos el sistema por $\mathbf U(s,\tau)=\mathbf U(\tau,s)^{-1}$.
Para abreviar tomamos inicialmente $s=0$ y definimos

```math
\mathbf z(\tau)=\mathbf U(0,\tau)\mathbf x(\tau).
```

Derivando,

```math
\mathbf z'
=\frac{d\mathbf U(0,\tau)}{d\tau}\mathbf x
+\mathbf U(0,\tau)\mathbf x'.
```

Como la derivada del inverso satisface

```math
\frac{d\mathbf U(0,\tau)}{d\tau}
=-\mathbf U(0,\tau)\mathbf A(\tau),
```

obtenemos

```math
\mathbf z'
=-\mathbf U(0,\tau)\mathbf A\mathbf x
+\mathbf U(0,\tau)
\left(\mathbf A\mathbf x+\mathbf b f\right).
```

Los términos homogéneos se cancelan:

```math
\mathbf z'(\tau)
=\mathbf U(0,\tau)\mathbf b f(\tau).
```

Integramos entre $0$ y $\tau$:

```math
\mathbf U(0,\tau)\mathbf x(\tau)-\mathbf x(0)
=\int_0^\tau
\mathbf U(0,s)\mathbf b f(s)\,ds.
```

Multiplicando por $\mathbf U(\tau,0)$,

```math
\boxed{
\mathbf x(\tau)
=\mathbf U(\tau,0)\mathbf x(0)
+\int_0^\tau
\mathbf U(\tau,s)\mathbf b f(s)\,ds
}.
```

### Comprobación

Si $f=0$, queda únicamente la evolución homogénea. Si además $\tau=0$,

```math
\mathbf U(0,0)\mathbf x(0)=\mathbf x(0),
```

como exige la condición inicial.

---

## Hoja M-003 — Salto impulsivo y núcleo causal de dos tiempos

**Fecha:** 11-08-2026

**Estado:** [DERIVADO]; causalidad y periodicidad verificadas automáticamente

### Problema

Encontrar la respuesta de la polarización a un impulso aplicado en $\tau=s$.

Tomamos

```math
f(\tau)=\delta(\tau-s).
```

### Paso 1 — Condiciones de salto

Integramos la ecuación escalar en un intervalo pequeño alrededor de $s$:

```math
\int_{s-\epsilon}^{s+\epsilon}p''\,d\tau
+2\zeta\int_{s-\epsilon}^{s+\epsilon}p'\,d\tau
+\int_{s-\epsilon}^{s+\epsilon}k(\tau)p\,d\tau
=1.
```

Al tomar $\epsilon\to0^+$, si $p$ y $k$ permanecen acotados,

```math
\int_{s-\epsilon}^{s+\epsilon}k(\tau)p\,d\tau\longrightarrow0.
```

Además,

```math
\int_{s-\epsilon}^{s+\epsilon}p''\,d\tau
=p'(s^+)-p'(s^-),
```

```math
\int_{s-\epsilon}^{s+\epsilon}p'\,d\tau
=p(s^+)-p(s^-).
```

La ausencia de una derivada de delta exige continuidad de $p$, de modo que

```math
p(s^+)-p(s^-)=0.
```

Por tanto,

```math
p'(s^+)-p'(s^-)=1.
```

El salto del estado es

```math
\mathbf x(s^+)-\mathbf x(s^-)
=\begin{pmatrix}0\\1\end{pmatrix}
=\mathbf b.
```

### Paso 2 — Respuesta retardada

Si el estado era nulo antes del impulso, para $\tau>s$ tenemos

```math
\mathbf x(\tau)=\mathbf U(\tau,s)\mathbf b.
```

La polarización es la primera componente. Con

```math
\mathbf e_p
=\begin{pmatrix}1\\0\end{pmatrix},
```

obtenemos el núcleo

```math
\boxed{
g(\tau,s)
=\mathbf e_p^{\mathsf T}
\mathbf U(\tau,s)\mathbf b
\Theta(\tau-s)
}.
```

### Paso 3 — Causalidad

Por construcción,

```math
g(\tau,s)=0,
\qquad
\tau\le s.
```

En el código se adopta el valor $\Theta(0)=0$ para el núcleo de polarización. El salto
ocurre en la velocidad, no en la polarización.

### Paso 4 — Periodicidad conjunta

Como

```math
\mathbf A(\tau+T_\tau)=\mathbf A(\tau),
```

las matrices

```math
\mathbf V(\tau,s)
=\mathbf U(\tau+T_\tau,s+T_\tau)
```

y $\mathbf U(\tau,s)$ satisfacen la misma ecuación diferencial y la misma condición
inicial en $\tau=s$. Por unicidad,

```math
\mathbf U(\tau+T_\tau,s+T_\tau)
=\mathbf U(\tau,s).
```

Luego

```math
\boxed{
g(\tau+T_\tau,s+T_\tau)=g(\tau,s)
}.
```

### Interpretación

El núcleo no depende únicamente de $\tau-s$. También depende de la fase de la
modulación en el instante $s$. Por eso es una respuesta de dos tiempos.

---

## Hoja M-004 — Función de Green exacta para $m=0$

**Fecha:** 11-08-2026

**Estado:** [VERIFICADO] mediante comparación con integración numérica

### Problema

Resolver

```math
g_0''(\Delta)
+2\zeta g_0'(\Delta)
+g_0(\Delta)
=\delta(\Delta),
```

con respuesta causal, donde

```math
\Delta=\tau-s.
```

### Paso 1 — Solución homogénea subamortiguada

Para $\Delta>0$ resolvemos

```math
r^2+2\zeta r+1=0.
```

Las raíces son

```math
r_\pm=-\zeta\pm\sqrt{\zeta^2-1}.
```

Si $0\le\zeta<1$, definimos

```math
\omega_d=\sqrt{1-\zeta^2},
```

de modo que

```math
r_\pm=-\zeta\pm\mathrm{i}\omega_d.
```

La solución causal para $\Delta>0$ tiene la forma

```math
g_0(\Delta)
=e^{-\zeta\Delta}
\left[A\cos(\omega_d\Delta)
+B\sin(\omega_d\Delta)\right].
```

### Paso 2 — Condiciones en el impulso

La continuidad de la polarización da

```math
g_0(0^+)=0,
```

por lo que $A=0$.

El salto de velocidad es unitario:

```math
g_0'(0^+)=1.
```

Como

```math
g_0'(0^+)=B\omega_d,
```

entonces

```math
B=\frac{1}{\omega_d}.
```

### Resultado

```math
\boxed{
g_0(\tau,s)
=\Theta(\tau-s)
e^{-\zeta(\tau-s)}
\frac{
\sin\left[\omega_d(\tau-s)\right]
}{\omega_d}
},
```

```math
\omega_d=\sqrt{1-\zeta^2}.
```

### Otros regímenes

Para $\zeta=1$,

```math
g_0(\Delta)=\Theta(\Delta)\,\Delta e^{-\Delta}.
```

Para $\zeta>1$, con $\alpha_d=\sqrt{\zeta^2-1}$,

```math
g_0(\Delta)
=\Theta(\Delta)e^{-\zeta\Delta}
\frac{\sinh(\alpha_d\Delta)}{\alpha_d}.
```

### Prueba usada en el código

La integración numérica del propagador para $m=0$ debe satisfacer

```math
\mathbf e_p^{\mathsf T}
\mathbf U(\tau,s)\mathbf b
=g_0(\tau,s)
```

dentro de la tolerancia numérica.

---

## Hoja M-005 — Monodromía, multiplicadores y estabilidad

**Fecha:** 11-08-2026

**Estado:** [VERIFICADO]

### Problema

Decidir si el sistema homogéneo periódico

```math
\mathbf x'=\mathbf A(\tau)\mathbf x
```

es estable.

### Paso 1 — Matriz fundamental

Definimos

```math
\boldsymbol\Phi'(\tau)
=\mathbf A(\tau)\boldsymbol\Phi(\tau),
\qquad
\boldsymbol\Phi(0)=\mathbf I.
```

La matriz monodrómica es

```math
\boxed{
\mathbf M=\boldsymbol\Phi(T_\tau)
}.
```

### Paso 2 — Evolución después de varios periodos

Por periodicidad,

```math
\boldsymbol\Phi(\tau+T_\tau)
=\boldsymbol\Phi(\tau)\mathbf M.
```

En particular,

```math
\mathbf x(N_cT_\tau)=\mathbf M^{N_c}\mathbf x(0),
\qquad N_c\in\mathbb N.
```

### Paso 3 — Multiplicadores

Los autovalores de $\mathbf M$ son

```math
\lambda_1,\lambda_2.
```

La tasa real asociada a cada multiplicador es

```math
\Gamma_j=\frac{\log|\lambda_j|}{T_\tau}.
```

Por tanto,

```math
\boxed{
\rho(\mathbf M)<1
\quad\Longleftrightarrow\quad
\text{estabilidad exponencial asintótica}
}
```

para este sistema periódico finito-dimensional.

### Paso 4 — Independencia de la fase inicial

La monodromía calculada desde una fase $\tau_0$ es

```math
\mathbf M(\tau_0)
=\mathbf U(\tau_0+T_\tau,\tau_0).
```

Para otra fase $\tau_1$, insertamos propagadores intermedios:

```math
\begin{aligned}
\mathbf M(\tau_1)
={}&
\mathbf U(\tau_1+T_\tau,\tau_0+T_\tau)
\mathbf U(\tau_0+T_\tau,\tau_0)
\mathbf U(\tau_0,\tau_1).
\end{aligned}
```

Por periodicidad conjunta,

```math
\mathbf U(\tau_1+T_\tau,\tau_0+T_\tau)
=\mathbf U(\tau_1,\tau_0),
```

y por inversión,

```math
\mathbf U(\tau_0,\tau_1)
=\mathbf U(\tau_1,\tau_0)^{-1}.
```

Luego

```math
\boxed{
\mathbf M(\tau_1)
=\mathbf U(\tau_1,\tau_0)
\mathbf M(\tau_0)
\mathbf U(\tau_1,\tau_0)^{-1}
}.
```

Las matrices pueden ser distintas, pero son semejantes. En consecuencia conservan
autovalores, traza y determinante.

### Advertencia sobre el logaritmo complejo

Si escribimos

```math
\mu_j=\frac{1}{T_\tau}\,\mathrm{Log}\,\lambda_j,
```

entonces

```math
\mu_j
\sim
\mu_j+\frac{2\pi\mathrm{i}\ell}{T_\tau},
\qquad \ell\in\mathbb Z.
```

La rama cambia la parte imaginaria, pero no cambia

```math
\mathrm{Re}\,\mu_j
=\frac{\log|\lambda_j|}{T_\tau}.
```

La estabilidad debe decidirse con $|\lambda_j|$, no con una rama arbitraria.

---

## Hoja M-006 — Demostración de la identidad de Liouville

**Fecha:** 11-08-2026

**Estado:** [VERIFICADO] con error menor que $10^{-13}$ en el benchmark

### Se quiere demostrar

```math
\det\mathbf M=e^{-2\zeta T_\tau}.
```

### Paso 1 — Fórmula de Jacobi

Para una matriz invertible $\boldsymbol\Phi(\tau)$,

```math
\frac{d}{d\tau}\det\boldsymbol\Phi
=\det\boldsymbol\Phi\,
\mathrm{tr}\!\left(
\boldsymbol\Phi^{-1}\boldsymbol\Phi'
\right).
```

Como

```math
\boldsymbol\Phi'=\mathbf A\boldsymbol\Phi,
```

tenemos

```math
\boldsymbol\Phi^{-1}\boldsymbol\Phi'
=\boldsymbol\Phi^{-1}\mathbf A\boldsymbol\Phi.
```

La traza es invariante bajo semejanza:

```math
\mathrm{tr}\!\left(
\boldsymbol\Phi^{-1}\mathbf A\boldsymbol\Phi
\right)
=\mathrm{tr}\,\mathbf A.
```

Por tanto,

```math
\frac{d}{d\tau}\det\boldsymbol\Phi
=\mathrm{tr}\,\mathbf A(\tau)
\det\boldsymbol\Phi.
```

### Paso 2 — Traza del sistema

Para

```math
\mathbf A(\tau)
=\begin{pmatrix}
0&1\\
-k(\tau)&-2\zeta
\end{pmatrix},
```

la traza es constante:

```math
\mathrm{tr}\,\mathbf A(\tau)=-2\zeta.
```

Entonces

```math
\frac{d}{d\tau}
\log\det\boldsymbol\Phi(\tau)
=-2\zeta.
```

Integramos desde $0$ hasta $T_\tau$:

```math
\log\det\boldsymbol\Phi(T_\tau)
-\log\det\boldsymbol\Phi(0)
=-2\zeta T_\tau.
```

Como

```math
\det\boldsymbol\Phi(0)=1,
```

queda

```math
\boxed{
\det\mathbf M=e^{-2\zeta T_\tau}
}.
```

### Lectura física

Si $\zeta>0$, el área de fase se contrae cada periodo. Sin embargo, esto no obliga
a que ambos multiplicadores tengan módulo menor que uno: una dirección puede crecer
mientras la otra se contrae con mayor rapidez.

---

## Hoja M-007 — Demostración del balance exacto de energía

**Fecha:** 11-08-2026

**Estado:** [VERIFICADO] numéricamente

### Definición

Tomamos la energía adimensional instantánea

```math
\mathcal E(\tau)
=\frac12v^2(\tau)
+\frac12k(\tau)p^2(\tau).
```

### Paso 1 — Derivación directa

Derivamos término por término:

```math
\frac{d\mathcal E}{d\tau}
=v v'
+\frac12k'p^2
+kp p'.
```

Usamos

```math
p'=v,
```

```math
v'=-kp-2\zeta v+f.
```

Sustituyendo,

```math
\frac{d\mathcal E}{d\tau}
=v(-kp-2\zeta v+f)
+\frac12k'p^2
+kpv.
```

Los términos $-kpv$ y $+kpv$ se cancelan:

```math
\boxed{
\frac{d\mathcal E}{d\tau}
=-2\zeta v^2
+\frac12k'(\tau)p^2
+v f
}.
```

### Paso 2 — Identificación de potencias

Definimos

```math
P_{\mathrm{dis}}=-2\zeta v^2,
```

```math
P_{\mathrm{mod}}=\frac12k'p^2,
```

```math
P_{\mathrm{in}}=vf.
```

Como

```math
k'=-m\nu\sin(\nu\tau+\phi),
```

el bombeo puede entregar o retirar energía según la fase instantánea de $p^2$.

### Paso 3 — Forma integral

Integrando desde $0$ hasta $\tau$,

```math
\mathcal E(\tau)-\mathcal E(0)
=W_{\mathrm{dis}}(\tau)
+W_{\mathrm{mod}}(\tau)
+W_{\mathrm{in}}(\tau),
```

donde

```math
W_j(\tau)=\int_0^\tau P_j(s)\,ds.
```

### Residuo usado en la prueba numérica

```math
r_E(\tau)
=\mathcal E(\tau)-\mathcal E(0)
-W_{\mathrm{dis}}(\tau)
-W_{\mathrm{mod}}(\tau)
-W_{\mathrm{in}}(\tau).
```

El cálculo debe satisfacer

```math
\max_\tau|r_E(\tau)|\longrightarrow0
```

al reducir las tolerancias y refinar la malla.

### Resultado conceptual

```math
\boxed{
\text{amplificación paramétrica}
\neq
\text{energía gratuita}
}
```

La energía adicional procede de $W_{\mathrm{mod}}$.

---

## Hoja M-008 — Umbral aproximado de la primera lengua de Mathieu

**Fecha:** 11-08-2026

**Estado:** [DERIVADO] por promediado de primer orden; contrastado numéricamente

### Problema

Explicar por qué aparece una región inestable cerca de

```math
\nu=2
```

y obtener el umbral aproximado de modulación.

Tomamos la ecuación homogénea

```math
p''+2\zeta p'
+\left[1+m\cos(\nu\tau+\phi)\right]p=0.
```

La fase $\phi$ desplaza el origen temporal y no cambia los multiplicadores. Para el
cálculo del umbral fijamos $\phi=0$.

### Paso 1 — Centro resonante de la aproximación de primer orden

Al primer orden, el centro de la primera resonancia se aproxima mediante

```math
\nu=2.
```

Suponemos que $m$, $\zeta$ y la variación de las amplitudes son pequeños. Escribimos

```math
p(\tau)=a(\tau)\cos\tau+b(\tau)\sin\tau,
```

donde $a'$ y $b'$ son de primer orden y se ignoran $a''$ y $b''$.

Entonces

```math
p'
\approx-a\sin\tau+b\cos\tau
+a'\cos\tau+b'\sin\tau,
```

y, conservando solo los términos lentos de primer orden,

```math
p''+p
\approx-2a'\sin\tau+2b'\cos\tau.
```

Reescribimos la ecuación como

```math
p''+p=-2\zeta p'-m\cos(2\tau)p.
```

### Paso 2 — Términos resonantes

Para el amortiguamiento usamos

```math
-2\zeta p'
\approx
2\zeta a\sin\tau-2\zeta b\cos\tau.
```

Para la modulación necesitamos

```math
\cos(2\tau)\cos\tau
=\frac12\left[\cos(3\tau)+\cos\tau\right],
```

```math
\cos(2\tau)\sin\tau
=\frac12\left[\sin(3\tau)-\sin\tau\right].
```

Los términos con $3\tau$ oscilan rápido y su promedio es cero. La parte resonante
de la modulación es

```math
-m\cos(2\tau)p
\rightsquigarrow
-\frac m2a\cos\tau
+\frac m2b\sin\tau.
```

Igualamos coeficientes de $\sin\tau$ y $\cos\tau$:

```math
-2a'=2\zeta a+\frac m2b,
```

```math
2b'=-2\zeta b-\frac m2a.
```

Por tanto,

```math
\begin{pmatrix}
a'\\b'
\end{pmatrix}
=
\begin{pmatrix}
-\zeta&-m/4\\
-m/4&-\zeta
\end{pmatrix}
\begin{pmatrix}
a\\b
\end{pmatrix}.
```

Los autovalores promediados son

```math
\Gamma_\pm^{\mathrm{av}}
=-\zeta\pm\frac{|m|}{4}.
```

Para $m>0$, la rama creciente es

```math
\Gamma_{\max}^{\mathrm{av}}
=-\zeta+\frac m4.
```

### Resultado en el centro

La aproximación predice inestabilidad cuando

```math
-\zeta+\frac m4>0.
```

Es decir,

```math
\boxed{m>4\zeta}.
```

### Paso 3 — Desintonía pequeña

Sea

```math
\nu=2+\delta,
\qquad
|\delta|\ll1.
```

Tomamos una base que gira con la mitad de la frecuencia de modulación:

```math
\theta=\frac{\nu\tau}{2},
\qquad
p=a(\tau)\cos\theta+b(\tau)\sin\theta.
```

Al repetir el promedio y conservar términos de primer orden en $m$, $\zeta$ y
$\delta$, se obtiene

```math
\begin{pmatrix}
a'\\b'
\end{pmatrix}
\approx
\begin{pmatrix}
-\zeta&-m/4-\delta/2\\
-m/4+\delta/2&-\zeta
\end{pmatrix}
\begin{pmatrix}
a\\b
\end{pmatrix}.
```

Sus tasas aproximadas son

```math
\boxed{
\Gamma_\pm^{\mathrm{av}}
\approx
-\zeta
\pm
\sqrt{
\left(\frac m4\right)^2
-\left(\frac\delta2\right)^2
}
}.
```

La primera lengua queda descrita aproximadamente por

```math
\left(\frac\delta2\right)^2+\zeta^2
<
\left(\frac m4\right)^2.
```

### Alcance de la aproximación

Este resultado es de primer orden. No debe usarse como frontera exacta cuando la
modulación es intensa o cuando se necesita resolver el desplazamiento de resonancia
de orden $\zeta^2$. Al eliminar primero el amortiguamiento, la frecuencia natural
de la ecuación transformada es $\sqrt{1-\zeta^2}$; por ello una aproximación más
precisa del centro, todavía sin correcciones superiores en $m$, es

```math
\nu_{\mathrm c}\approx2\sqrt{1-\zeta^2}.
```

---

## Hoja M-009 — Cálculo de los benchmarks

**Fecha:** 11-08-2026

**Estado:** [VERIFICADO] numéricamente

### A. Benchmark inestable

Usamos

```math
\zeta=0.02,
\qquad
m=0.20,
\qquad
\nu=2,
\qquad
\phi=0.
```

El periodo es

```math
T_\tau=\frac{2\pi}{2}=\pi.
```

La aproximación de la hoja M-008 predice

```math
\Gamma_{\max}^{\mathrm{av}}
=-0.02+\frac{0.20}{4}
=0.03.
```

La integración de la matriz fundamental produce

```math
\mathbf M_{\mathrm{num}}
\approx
\begin{pmatrix}
-0.9477618712&0.1462576703\\
0.1496392219&-0.9536121780
\end{pmatrix}.
```

Los multiplicadores son

```math
\lambda_1\approx-1.0986547255,
```

```math
\lambda_2\approx-0.8027193238.
```

El radio espectral vale

```math
\rho(\mathbf M)=1.0986547255>1.
```

La tasa calculada es

```math
\Gamma_{\max}
=\frac{\log(1.0986547255)}{\pi}
\approx0.0299486486.
```

La diferencia respecto del promediado es

```math
|0.03-0.0299486486|
\approx5.14\times10^{-5}.
```

### Prueba de Liouville para el caso inestable

El valor exacto esperado es

```math
e^{-2\zeta T_\tau}
=e^{-0.04\pi}
\approx0.8819113782981763.
```

El valor numérico es

```math
\det\mathbf M_{\mathrm{num}}
\approx0.8819113782980792.
```

Por tanto,

```math
\left|
\det\mathbf M_{\mathrm{num}}
-e^{-2\zeta T_\tau}
\right|
\approx9.71\times10^{-14}.
```

Aunque el determinante es menor que uno, el sistema es inestable porque uno de los
multiplicadores tiene módulo mayor que uno.

### Prueba energética

El residuo normalizado del balance de energía obtenido en el experimento es del
orden de

```math
3.6\times10^{-10}.
```

En el horizonte de $30$ periodos usado por el experimento, el trabajo neto final
del modulador es positivo:

```math
W_{\mathrm{mod}}(\tau_f)
\approx120.8268424>0.
```

Esto no significa que el trabajo acumulado ni la potencia instantánea sean siempre
positivos. De hecho, en esa misma trayectoria,

```math
\min_{0\le\tau\le\tau_f}
W_{\mathrm{mod}}(\tau)
\approx-0.09181365.
```

La afirmación correcta es que la modulación entrega energía neta al final del
horizonte observado.

### B. Benchmark estable

Conservamos

```math
\zeta=0.02,
\qquad
m=0.20,
\qquad
\phi=0,
```

pero cambiamos a

```math
\nu=3.
```

El periodo pasa a ser

```math
T_\tau=\frac{2\pi}{3}
\approx2.0943951024.
```

La monodromía numérica es

```math
\mathbf M_{\mathrm{num}}
\approx
\begin{pmatrix}
-0.4646813057&0.8969211047\\
-0.7659953520&-0.5005581499
\end{pmatrix}.
```

Los multiplicadores forman un par conjugado:

```math
\lambda_{1,2}
\approx
-0.4826197278
\mp0.8286830578\,\mathrm{i}.
```

Su módulo es

```math
|\lambda_{1,2}|
\approx0.9589772739<1.
```

Como forman un par conjugado,

```math
|\lambda_1|^2
=\lambda_1\lambda_2
=\det\mathbf M
=e^{-2\zeta T_\tau}.
```

Luego

```math
|\lambda_1|=e^{-\zeta T_\tau},
```

y la tasa es

```math
\Gamma_{1,2}
=\frac{\log|\lambda_{1,2}|}{T_\tau}
=-\zeta
=-0.02.
```

### Resultado de la hoja

```math
\boxed{
\begin{aligned}
\nu=2&:\quad\Gamma_{\max}\approx0.02994865>0,\\
\nu=3&:\quad\Gamma_{\max}\approx-0.02<0.
\end{aligned}
}
```

El caso $\nu=3$ será el banco de pruebas del canal armónico de horizonte largo.

---

## Hoja M-010 — Cota exponencial del propagador estable

**Fecha:** 11-08-2026

**Estado:** [VERIFICADO] analíticamente para el sistema finito-dimensional

### Se quiere demostrar

Si

```math
\rho(\mathbf M)<1,
```

entonces existen constantes $C>0$ y $\alpha>0$ tales que

```math
\boxed{
\|\mathbf U(\tau,s)\|
\le
C e^{-\alpha(\tau-s)},
\qquad
\tau\ge s
}.
```

### Paso 1 — Potencias de la monodromía

Elegimos un número $r$ que satisfaga

```math
\rho(\mathbf M)<r<1.
```

En dimensión finita existe $C_M>0$ tal que

```math
\|\mathbf M^{N_c}\|
\le C_Mr^{N_c},
\qquad
N_c=0,1,2,\ldots
```

Esta afirmación sigue de la forma de Jordan o, de manera equivalente, de escoger
una norma matricial adaptada y absorber en $C_M$ el posible crecimiento polinómico
de bloques no normales.

### Paso 2 — Monodromía desde una fase arbitraria

Definimos

```math
\mathbf M_s=\mathbf U(s+T_\tau,s).
```

Si reducimos $s$ a un periodo, entonces

```math
\mathbf M_s
=\mathbf U(s,0)
\mathbf M
\mathbf U(s,0)^{-1}.
```

Por tanto, todas las $\mathbf M_s$ son semejantes y tienen el mismo espectro.
Además, como $s$ recorre un intervalo compacto y el propagador es continuo,

```math
\sup_{0\le s\le T_\tau}
\|\mathbf U(s,0)\|
\|\mathbf U(s,0)^{-1}\|
<\infty.
```

En consecuencia existe una constante uniforme $C_1$ con

```math
\|\mathbf M_s^{N_c}\|
\le C_1r^{N_c}.
```

### Paso 3 — Separar periodos completos y residuo

Escribimos

```math
\tau-s=N_cT_\tau+\sigma,
\qquad
0\le\sigma<T_\tau.
```

Por composición y periodicidad,

```math
\mathbf U(\tau,s)
=\mathbf U(s+\sigma,s)\mathbf M_s^{N_c}.
```

La evolución dentro de un solo periodo está uniformemente acotada:

```math
C_B
=\sup_{
0\le s\le T_\tau,
\ 0\le\sigma\le T_\tau
}
\|\mathbf U(s+\sigma,s)\|
<\infty.
```

Así,

```math
\|\mathbf U(\tau,s)\|
\le C_BC_1r^{N_c}.
```

Como

```math
N_c\ge\frac{\tau-s}{T_\tau}-1,
```

y $0<r<1$,

```math
r^{N_c}
\le
r^{-1}
\exp\left[
\frac{\log r}{T_\tau}(\tau-s)
\right].
```

Definimos

```math
\alpha=-\frac{\log r}{T_\tau}>0,
```

```math
C=C_BC_1r^{-1}.
```

Obtenemos la cota buscada.

### Consecuencia para el núcleo

Como

```math
g(\tau,s)
=\mathbf e_p^{\mathsf T}
\mathbf U(\tau,s)\mathbf b
\Theta(\tau-s),
```

entonces

```math
|g(\tau,s)|
\le
\|\mathbf e_p\|\,\|\mathbf b\|\,
C e^{-\alpha(\tau-s)}
\Theta(\tau-s).
```

Esta cota justifica, para entradas adecuadas, la integral desde el pasado remoto
que aparecerá en la comparación tiempo–Floquet.

### Pendiente de esta hoja

La demostración deberá generalizarse posteriormente al operador Maxwell–Lorentz
espacial, donde la elección del espacio funcional y del dominio del generador ya no
es automática.

---

## Hoja M-011 — Balance armónico del Lorentz modulado

**Fecha:** 11-08-2026

**Estado:** [DERIVADO]; implementación pendiente

### Problema

Transformar

```math
p''+2\zeta p'
+\left[1+m\cos(\nu\tau+\phi)\right]p=f
```

en un sistema algebraico que acople bandas laterales de Floquet.

### Paso 1 — Expansiones

Elegimos una cuasifrecuencia $\varpi$ dentro de una zona fundamental, por ejemplo

```math
\mathcal B_\nu
=\left[-\frac\nu2,\frac\nu2\right).
```

Escribimos

```math
p(\tau)
=\sum_{n\in\mathbb Z}
P_n(\varpi)
e^{-\mathrm{i}(\varpi+n\nu)\tau},
```

```math
f(\tau)
=\sum_{n\in\mathbb Z}
F_n(\varpi)
e^{-\mathrm{i}(\varpi+n\nu)\tau}.
```

Definimos

```math
\omega_n=\varpi+n\nu.
```

### Paso 2 — Derivadas

Usando la convención de la hoja M-000,

```math
p'
=\sum_n
(-\mathrm{i}\omega_n)P_n
e^{-\mathrm{i}\omega_n\tau},
```

```math
p''
=\sum_n
(-\omega_n^2)P_n
e^{-\mathrm{i}\omega_n\tau}.
```

La parte no modulada aporta

```math
\sum_n
\left(
1-\omega_n^2-2\mathrm{i}\zeta\omega_n
\right)
P_n e^{-\mathrm{i}\omega_n\tau}.
```

Definimos

```math
\boxed{
D_n(\varpi)
=1-(\varpi+n\nu)^2
-2\mathrm{i}\zeta(\varpi+n\nu)
}.
```

### Paso 3 — Producto con la modulación

Descomponemos

```math
\cos(\nu\tau+\phi)
=\frac12
e^{\mathrm{i}\phi}e^{\mathrm{i}\nu\tau}
+\frac12
e^{-\mathrm{i}\phi}e^{-\mathrm{i}\nu\tau}.
```

El primer exponencial produce

```math
e^{\mathrm{i}\phi}e^{\mathrm{i}\nu\tau}p(\tau)
=\sum_k
e^{\mathrm{i}\phi}P_k
e^{-\mathrm{i}[\varpi+(k-1)\nu]\tau}.
```

Para recoger el armónico $n$ imponemos

```math
k-1=n,
```

por lo que

```math
k=n+1.
```

La contribución correspondiente es

```math
e^{\mathrm{i}\phi}P_{n+1}.
```

El segundo exponencial produce

```math
e^{-\mathrm{i}\phi}e^{-\mathrm{i}\nu\tau}p(\tau)
=\sum_k
e^{-\mathrm{i}\phi}P_k
e^{-\mathrm{i}[\varpi+(k+1)\nu]\tau}.
```

Ahora imponemos

```math
k+1=n,
```

de donde

```math
k=n-1.
```

La segunda contribución es

```math
e^{-\mathrm{i}\phi}P_{n-1}.
```

### Resultado por armónico

Al igualar el coeficiente de

```math
e^{-\mathrm{i}(\varpi+n\nu)\tau},
```

obtenemos

```math
\boxed{
D_n(\varpi)P_n
+\frac m2
\left(
e^{-\mathrm{i}\phi}P_{n-1}
+e^{\mathrm{i}\phi}P_{n+1}
\right)
=F_n
}.
```

### Control de signos

Con $e^{-\mathrm{i}\omega\tau}$:

- $P_{n-1}$ lleva $e^{-\mathrm{i}\phi}$;
- $P_{n+1}$ lleva $e^{\mathrm{i}\phi}$;
- el amortiguamiento entra como $-2\mathrm{i}\zeta\omega_n$.

Invertir la convención temporal invertiría estos signos de fase. Por eso esta línea
debe permanecer asociada a la hoja M-000.

### Prueba perturbativa de las fases

Tomamos una entrada únicamente en el armónico central:

```math
F_n=F_0\delta_{n0},
```

y suponemos $|m|\ll1$.

Para que el conteo en potencias de $m$ sea uniforme, suponemos además que
$D_0$, $D_{1}$ y $D_{-1}$ permanecen separados de cero y que el operador
diagonal no modulado tiene inversa acotada en las bandas consideradas. En
particular, existe una constante $d_*>0$, independiente de $m$, tal que

```math
|D_0|,\ |D_1|,\ |D_{-1}|\ge d_*.
```

Cerca de una singularidad o de un régimen fuertemente mal condicionado, las
estimaciones $O(m)$ y $O(m^2)$ siguientes dejan de ser uniformes y esta prueba no
puede usarse sin un reescalamiento resonante. Bajo la hipótesis anterior, a orden
cero,

```math
P_0=\frac{F_0}{D_0}+O(m^2).
```

En la fila $n=1$, despreciando $P_2=O(m^2)$,

```math
D_1P_1+\frac m2e^{-\mathrm{i}\phi}P_0=O(m^2).
```

Por tanto,

```math
\boxed{
P_1
=-\frac m2
\frac{e^{-\mathrm{i}\phi}F_0}{D_1D_0}
+O(m^2)
}.
```

En la fila $n=-1$,

```math
D_{-1}P_{-1}
+\frac m2e^{\mathrm{i}\phi}P_0
=O(m^2),
```

de donde

```math
\boxed{
P_{-1}
=-\frac m2
\frac{e^{\mathrm{i}\phi}F_0}{D_{-1}D_0}
+O(m^2)
}.
```

Estas dos fórmulas se convertirán en pruebas automáticas. Un intercambio de fases
hará que fallen aun cuando los módulos parezcan correctos.

---

## Hoja M-012 — Truncamiento y matriz de transferencia de Floquet

**Fecha:** 11-08-2026

**Estado:** [DERIVADO]; implementación pendiente

### Paso 1 — Truncamiento

Retenemos

```math
-N_F\le n\le N_F.
```

La dimensión es

```math
N_b=2N_F+1.
```

En el sistema proyectado usamos la extensión por cero

```math
P_n=0,
\qquad
|n|>N_F.
```

Esta igualdad define únicamente la aproximación de Galerkin fuera del subespacio
retenido. No afirma que los coeficientes físicos exactos del problema infinito sean
cero.

Definimos

```math
a_-=\frac m2e^{-\mathrm{i}\phi},
\qquad
a_+=\frac m2e^{\mathrm{i}\phi}.
```

### Paso 2 — Ejemplo para $N_F=1$

El vector de incógnitas es

```math
\mathbf P^{(1)}
=\begin{pmatrix}
P_{-1}\\P_0\\P_1
\end{pmatrix}.
```

El sistema es

```math
\begin{pmatrix}
D_{-1}&a_+&0\\
a_-&D_0&a_+\\
0&a_-&D_1
\end{pmatrix}
\begin{pmatrix}
P_{-1}\\P_0\\P_1
\end{pmatrix}
=
\begin{pmatrix}
F_{-1}\\F_0\\F_1
\end{pmatrix}.
```

### Paso 3 — Definición general

Llamamos $\mathsf L_{N_F}(\varpi)$ a la matriz dinámica, para no confundirla con
la monodromía $\mathbf M$. Sus elementos son

```math
\begin{aligned}
[\mathsf L_{N_F}]_{n\ell}
={}&D_n\delta_{n\ell}
+a_-\delta_{\ell,n-1}
+a_+\delta_{\ell,n+1},\\
&-N_F\le n,\ell\le N_F.
\end{aligned}
```

El sistema truncado es

```math
\mathsf L_{N_F}(\varpi)
\mathbf P^{(N_F)}(\varpi)
=\mathbf F^{(N_F)}(\varpi).
```

Si la matriz es invertible, definimos la transferencia armónica

```math
\boxed{
\mathsf H_F^{(N_F)}(\varpi)
=\mathsf L_{N_F}(\varpi)^{-1}
}.
```

Entonces

```math
\mathbf P^{(N_F)}
=\mathsf H_F^{(N_F)}\mathbf F^{(N_F)}.
```

### Caso límite $m=0$

Si

```math
m=0,
```

entonces

```math
a_-=a_+=0
```

y la matriz se vuelve diagonal:

```math
\mathsf L_{N_F}
=\mathrm{diag}
\left(
D_{-N_F},\ldots,D_0,\ldots,D_{N_F}
\right).
```

Por tanto,

```math
\boxed{
P_n=\frac{F_n}{D_n}
}.
```

Esta será la primera prueba exacta de la implementación.

### Covarianza respecto de la fase

Definimos la matriz diagonal

```math
\mathsf S_\phi
=\mathrm{diag}
\left(e^{-\mathrm{i}n\phi}\right)_{n=-N_F}^{N_F}.
```

La estructura de las diagonales implica

```math
\boxed{
\mathsf L_{N_F}(\phi)
=\mathsf S_\phi
\mathsf L_{N_F}(0)
\mathsf S_\phi^{-1}
}.
```

Por inversión,

```math
\mathsf H_F^{(N_F)}(\phi)
=\mathsf S_\phi
\mathsf H_F^{(N_F)}(0)
\mathsf S_\phi^{-1}.
```

Si la entrada solo ocupa $n=0$, entonces

```math
\boxed{
P_n(\phi)=e^{-\mathrm{i}n\phi}P_n(0)
}.
```

Esta identidad será una segunda prueba independiente de los signos de fase.

### Diagnóstico de borde

El truncamiento será sospechoso si los últimos armónicos todavía llevan amplitud
apreciable. Para una fibra $\varpi$ definimos

```math
r_{\mathrm{borde}}^{(N_F)}
=\frac{
|P_{-N_F}|^2+|P_{N_F}|^2
}{
\displaystyle\sum_{n=-N_F}^{N_F}|P_n|^2
}.
```

Si la solución es idénticamente nula, el cociente se registra por convenio como
cero y se informa por separado que no hubo respuesta.

El objetivo numérico es verificar simultáneamente

```math
r_{\mathrm{borde}}^{(N_F)}\longrightarrow0
```

y convergencia de la señal reconstruida.

### Residuo exterior de la ecuación

Definimos primero la salida y la entrada proyectadas sobre el mismo subespacio:

```math
p_{N_F}(\tau;\varpi)
=\sum_{|n|\le N_F}
P_n(\varpi)e^{-\mathrm{i}(\varpi+n\nu)\tau},
```

```math
f_{N_F}(\tau;\varpi)
=\sum_{|n|\le N_F}
F_n(\varpi)e^{-\mathrm{i}(\varpi+n\nu)\tau}.
```

Sea el operador diferencial

```math
\mathcal D_\phi
=\frac{d^2}{d\tau^2}
+2\zeta\frac{d}{d\tau}
+1+m\cos(\nu\tau+\phi).
```

El residuo de la ecuación completa es

```math
\boxed{
r_{N_F}(\tau;\varpi)
=\mathcal D_\phi p_{N_F}(\tau;\varpi)
-f_{N_F}(\tau;\varpi)
}.
```

Las ecuaciones proyectadas anulan exactamente los coeficientes retenidos. Como la
modulación sinusoidal solo desplaza el índice en una unidad, quedan dos bandas
exteriores:

```math
\begin{aligned}
r_{N_F}(\tau)
={}&
\frac m2e^{-\mathrm{i}\phi}P_{N_F}
e^{-\mathrm{i}[\varpi+(N_F+1)\nu]\tau}\\
&+
\frac m2e^{\mathrm{i}\phi}P_{-N_F}
e^{-\mathrm{i}[\varpi-(N_F+1)\nu]\tau}.
\end{aligned}
```

Por ortogonalidad durante un periodo,

```math
\boxed{
\frac{1}{T_\tau}
\int_{\tau_0}^{\tau_0+T_\tau}
|r_{N_F}(\tau)|^2\,d\tau
=\frac{m^2}{4}
\left(
|P_{N_F}|^2+|P_{-N_F}|^2
\right)
}.
```

Esta identidad convierte la amplitud de borde en un residuo explícito de la ecuación,
no en una energía física. Para interpretar una energía habría que introducir pesos
dependientes de las frecuencias $\varpi+n\nu$.

La fórmula de dos bandas es exacta para la entrada proyectada $f_{N_F}$. Si se
compara contra una entrada infinita con coeficientes exteriores, los dos primeros
coeficientes pasan a ser

```math
\frac m2e^{-\mathrm{i}\phi}P_{N_F}-F_{N_F+1},
\qquad
\frac m2e^{\mathrm{i}\phi}P_{-N_F}-F_{-N_F-1},
```

y para $|n|>N_F+1$ también aparece el residuo $-F_n$. Además, cerca de una matriz
mal condicionada, un residuo pequeño no garantiza por sí solo un error pequeño.

### Comparación entre truncamientos

No podemos restar directamente matrices de dimensiones distintas. La comparación
correcta usa una proyección al espacio común:

```math
\delta_{N_F}
=\left\|
\mathsf P_{N_F}
\mathsf H_F^{(N_F+1)}
\mathsf P_{N_F}^{\mathsf T}
-\mathsf H_F^{(N_F)}
\right\|.
```

Aquí $\mathsf P_{N_F}$ selecciona los índices $-N_F,\ldots,N_F$ de la matriz más
grande.

---

## Hoja M-013 — Protocolo de equivalencia tiempo–Floquet

**Fecha:** 11-08-2026

**Estado principal:** [DERIVADO] formalmente; implementación y ejecución [PENDIENTE]

- **Puente núcleo–serie para un tono:** [DERIVADO] bajo las hipótesis indicadas.
- **Experimento comparativo tiempo–Floquet:** [PENDIENTE].
- **Convergencia cuando $N_F\to\infty$:** [HIPÓTESIS].

### Pregunta falsable

¿La integral causal y la matriz armónica truncada predicen la misma salida estable?

### Representación temporal

En el régimen estrictamente estable, para una entrada admisible; por ejemplo,
$f\in L^\infty(\mathbb R)$ con $|f(s)|\le F_{\max}$, la solución acotada de régimen
es

```math
\boxed{
p_{\mathrm{tiempo}}(\tau)
=\int_{-\infty}^{\tau}
g(\tau,s)f(s)\,ds
}.
```

En efecto, si

```math
K=\|\mathbf e_p\|\,\|\mathbf b\|\,C,
```

la cota de la hoja M-010 implica

```math
|g(\tau,s)|
\le K e^{-\alpha(\tau-s)},
\qquad
s\le\tau,
```

y por tanto la integral converge absolutamente:

```math
\int_{-\infty}^{\tau}
|g(\tau,s)f(s)|\,ds
\le\frac{KF_{\max}}{\alpha}.
```

La estabilidad exponencial y la clase de entrada son ambas necesarias; causalidad
por sí sola no basta para integrar desde $-\infty$.

### Puente exacto para un tono

Consideramos primero

```math
f(s)=F_0e^{-\mathrm{i}\varpi s}.
```

La solución causal acotada es

```math
p_{\mathrm{ss}}(\tau)
=F_0\int_{-\infty}^{\tau}
g(\tau,s)e^{-\mathrm{i}\varpi s}\,ds.
```

Hacemos el cambio

```math
u=\tau-s,
\qquad
s=\tau-u,
\qquad
ds=-du.
```

Los límites se transforman según

```math
s=-\infty\Longrightarrow u=+\infty,
\qquad
s=\tau\Longrightarrow u=0.
```

Por tanto,

```math
\begin{aligned}
p_{\mathrm{ss}}(\tau)
={}&F_0e^{-\mathrm{i}\varpi\tau}
\int_0^\infty
g(\tau,\tau-u)e^{\mathrm{i}\varpi u}\,du.
\end{aligned}
```

Definimos la envolvente periódica

```math
Q_\varpi(\tau)
=F_0
\int_0^\infty
g(\tau,\tau-u)e^{\mathrm{i}\varpi u}\,du.
```

Usando la periodicidad conjunta,

```math
g(\tau+T_\tau,\tau+T_\tau-u)
=g(\tau,\tau-u),
```

obtenemos

```math
Q_\varpi(\tau+T_\tau)=Q_\varpi(\tau).
```

La envolvente admite una serie de Fourier:

```math
Q_\varpi(\tau)
=\sum_{n\in\mathbb Z}
P_n(\varpi)e^{-\mathrm{i}n\nu\tau}.
```

Finalmente,

```math
\boxed{
p_{\mathrm{ss}}(\tau)
=\sum_{n\in\mathbb Z}
P_n(\varpi)
e^{-\mathrm{i}(\varpi+n\nu)\tau}
}.
```

La sustitución término a término requiere declarar el alcance. Suponemos
$\varpi\in\mathbb R$, estabilidad exponencial, coeficientes periódicos suaves y
convergencia suficiente de la serie de Fourier y de sus dos primeras derivadas para
intercambiar suma, derivación e integral impropia. Bajo estas hipótesis recuperamos
la recurrencia de la hoja M-011. Sin ellas, la igualdad debe entenderse solo en
sentido formal o débil.

Este es el puente matemático entre el núcleo causal y la representación de Floquet;
lo que falta medir es la convergencia del truncamiento.

### Representación armónica para una fibra

Para una cuasifrecuencia fija $\varpi$,

```math
\mathbf P^{(N_F)}(\varpi)
=\mathsf H_F^{(N_F)}(\varpi)
\mathbf F^{(N_F)}(\varpi).
```

La reconstrucción compleja es

```math
p_{\mathrm F}^{(N_F)}(\tau;\varpi)
=\sum_{n=-N_F}^{N_F}
P_n(\varpi)
e^{-\mathrm{i}(\varpi+n\nu)\tau}.
```

La comparación debe hacerse entre dos señales complejas o entre dos señales reales,
nunca entre representaciones distintas. Si se usa una excitación real, las fibras
deben respetar la simetría conjugada

```math
F_n(-\varpi)=F_{-n}(\varpi)^*,
\qquad
P_n(-\varpi)=P_{-n}(\varpi)^*.
```

La señal real se reconstruye incluyendo el par completo de frecuencias conjugadas.
Tomar solo la parte real de una reconstrucción unilateral sin corregir su
normalización puede cambiar la amplitud por un factor dos.

### Pulsos y señales de banda ancha

Un pulso no pertenece a una sola cuasifrecuencia. Debemos integrar todas las fibras
de la zona fundamental:

```math
F_n(\varpi)
=\widehat f(\varpi+n\nu),
\qquad
\varpi\in\mathcal B_\nu.
```

Para que la comparación de truncamientos use exactamente la misma entrada, fijamos
un índice de entrada $N_{\mathrm{in}}$ y definimos

```math
\boxed{
f_{N_{\mathrm{in}}}(\tau)
=\frac{1}{2\pi}
\int_{\mathcal B_\nu}
\sum_{|n|\le N_{\mathrm{in}}}
F_n(\varpi)e^{-\mathrm{i}(\varpi+n\nu)\tau}
\,d\varpi
}.
```

Para todo $N_F\ge N_{\mathrm{in}}$, imponemos $F_n=0$ cuando
$|n|>N_{\mathrm{in}}$. El integrador temporal y el solucionador armónico reciben
el mismo $f_{N_{\mathrm{in}}}$, sin ampliar su banda al aumentar $N_F$.

Para cada $\varpi$ resolvemos

```math
\mathbf P^{(N_F)}(\varpi)
=\mathsf H_F^{(N_F)}(\varpi)
\mathbf F^{(N_F)}(\varpi),
```

y después reconstruimos

```math
p_{\mathrm F}^{(N_F)}(\tau)
=\frac{1}{2\pi}
\int_{\mathcal B_\nu}
\sum_{n=-N_F}^{N_F}
P_n(\varpi)
e^{-\mathrm{i}(\varpi+n\nu)\tau}
\,d\varpi.
```

Resolver una única matriz $\mathsf L_{N_F}(\varpi)$ no basta para una entrada
pulsada.

Si el pulso original no es de banda compacta, primero elegiremos
$N_{\mathrm{in}}$ mediante una tolerancia independiente para la energía omitida y
después lo mantendremos fijo. Aumentar simultáneamente el ancho de banda de la
entrada y $N_F$ mezclaría el error de truncamiento del operador con el error de
representación de la entrada.

### Igualación de condiciones iniciales

La matriz armónica representa una solución acotada de régimen. No debe compararse
directamente con una integración iniciada en $\tau=0$ con estado arbitrario.

Tenemos dos opciones correctas:

1. inicializar el estado temporal con la historia previa,

   ```math
   \mathbf x(\tau_0)
   =\int_{-\infty}^{\tau_0}
   \mathbf U(\tau_0,s)\mathbf b f(s)\,ds;
   ```

2. integrar durante suficientes periodos y descartar el transitorio antes de medir.

La primera opción es conceptualmente exacta; la segunda es más sencilla para la
primera implementación.

Si la integración se inicia en $\tau_0$ con estado nulo, el término omitido del
pasado remoto en la salida es

```math
\Delta p_{\mathrm{pasado}}(\tau)
=\int_{-\infty}^{\tau_0}
g(\tau,s)f(s)\,ds.
```

Para $|f(s)|\le F_{\max}$, su magnitud satisface la cota explícita

```math
\boxed{
|\Delta p_{\mathrm{pasado}}(\tau)|
\le
\frac{KF_{\max}}{\alpha}
e^{-\alpha(\tau-\tau_0)}
}.
```

Por tanto, el número de periodos descartados no se elegirá solo visualmente: deberá
hacer que esta cota, o una estimación numérica más ajustada del mismo transitorio,
quede por debajo de la tolerancia registrada.

### Métrica principal

Sobre una ventana de observación $\mathcal I$ posterior al transitorio definimos

```math
\boxed{
\epsilon_{N_F}
=\frac{
\left\|
p_{\mathrm{tiempo}}
-p_{\mathrm F}^{(N_F)}
\right\|_{L^2(\mathcal I)}
}{
\left\|p_{\mathrm{tiempo}}\right\|_{L^2(\mathcal I)}
}
}.
```

Exigimos

```math
\|p_{\mathrm{tiempo}}\|_{L^2(\mathcal I)}>0.
```

Las dos funciones del cociente serán ambas complejas o ambas reales según el
protocolo elegido. Para tonos, $\mathcal I$ contendrá un número entero de periodos
de modulación; además se registrarán la discretización temporal, el transitorio
descartado y el error de cuadratura de la integral en $\varpi$.

### Hipótesis que se pondrá a prueba

```math
\boxed{
\epsilon_{N_F}\longrightarrow0
\quad\text{cuando}\quad
N_F\longrightarrow\infty
}.
```

No exigiremos disminución monótona paso a paso, porque un método de Galerkin puede
oscilar entre truncamientos y aun así converger. Además del error contra la
referencia temporal comprobaremos el criterio de Cauchy

```math
\left\|
p_{\mathrm F}^{(N_F+1)}
-p_{\mathrm F}^{(N_F)}
\right\|_{L^2(\mathcal I)}
\longrightarrow0.
```

Para coeficientes sinusoidales analíticos y parámetros alejados del umbral,
investigaremos si existe un régimen aproximadamente exponencial,

```math
\epsilon_{N_F}
\lesssim
A e^{-\beta N_F}.
```

Esta última expresión es una hipótesis de trabajo, no un resultado demostrado.

### Pruebas mínimas antes de aceptar el hito

1. **Límite estacionario:** para $m=0$, la solución armónica debe coincidir con
   $P_n=F_n/D_n$.
2. **Error retrospectivo algebraico:**

   ```math
   r_{\mathrm{back}}
   =\frac{
   \|\mathsf L_{N_F}\mathbf P-\mathbf F\|_2
   }{
   \|\mathsf L_{N_F}\|_2\|\mathbf P\|_2
   +\|\mathbf F\|_2
   }
   ```

   debe ser cercano a precisión de máquina cuando el sistema esté bien
   condicionado. Si numerador y denominador son simultáneamente cero, definimos
   $r_{\mathrm{back}}=0$ y registramos el caso nulo explícitamente.
3. **Convergencia:** $\epsilon_{N_F}$ y la diferencia entre truncamientos deben
   mostrar tendencia hacia cero y estabilizarse dentro de la tolerancia; no se
   exige monotonicidad entre cada par de valores consecutivos.
4. **Borde:** $r_{\mathrm{borde}}^{(N_F)}$ debe ser pequeño.
5. **Parseval para una fibra:** para $\varpi\in\mathbb R$ y la reconstrucción
   compleja completa,

   ```math
   \frac{1}{T_\tau}
   \int_{\tau_0}^{\tau_0+T_\tau}
   |p_{\mathrm F}^{(N_F)}(\tau;\varpi)|^2\,d\tau
   =\sum_{n=-N_F}^{N_F}|P_n(\varpi)|^2.
   ```

   La igualdad no se transfiere automáticamente a una reconstrucción unilateral
   después de tomar su parte real.

6. **Condicionamiento:** registrar

   ```math
   \kappa_2\!\left(\mathsf L_{N_F}\right)
   ```

   junto con los errores; un residual pequeño no basta si la matriz está mal
   condicionada.
7. **Muestreo:** si el paso en tiempo adimensional es $\Delta\tau$, la frecuencia
   angular de Nyquist es

   ```math
   \omega_{\mathrm{Nyq}}=\frac{\pi}{\Delta\tau}.
   ```

   Para reconstruir la solución truncada basta cubrir $|n|\le N_F$; para medir el
   residuo exterior deben cubrirse también las bandas $|n|=N_F+1$. Por ello usamos

   ```math
   \omega_{\mathrm{Nyq}}
   >
   \max_{|n|\le N_F+1}|\varpi+n\nu|.
   ```

   La referencia temporal contiene, en principio, más bandas. Se refinará
   $\Delta\tau$ hasta que el error medido sea estable, dejando además un margen
   sobre este mínimo.

8. **Fase:** no se permitirá ajustar posteriormente una fase o desplazar una señal
   para reducir el error; ambas representaciones deben usar el mismo origen temporal
   y el mismo $\phi$. El caso $\phi=0$ sirve como referencia, pero no detecta un
   intercambio de los factores $e^{\pm\mathrm{i}\phi}$. Es obligatoria una segunda
   prueba con

   ```math
   \phi=0.37,
   \qquad
   P_n(0.37)=e^{-0.37\mathrm{i}n}P_n(0),
   ```

   además de las identidades perturbativas de la hoja M-011.
9. **Benchmark:** la primera comparación se hará con

   ```math
   \zeta=0.02,
   \qquad
   m=0.20,
   \qquad
   \nu=3,
   \qquad
   \phi\in\{0,\ 0.37\}.
   ```

10. **Entrada fija:** se registrarán $N_{\mathrm{in}}$ y la energía espectral
    omitida. Todos los valores $N_F\ge N_{\mathrm{in}}$ usarán exactamente la misma
    entrada en ambos solucionadores.

El caso $\nu=2$ no se usará para una respuesta de régimen de horizonte infinito,
porque $\rho(\mathbf M)>1$.

### Entregables de la siguiente etapa

- módulo que construya $\mathsf L_{N_F}(\varpi)$;
- pruebas del límite $m=0$ y de las fases de acoplamiento;
- comparación de una entrada sinusoidal y una multisinusoidal;
- extensión posterior a un pulso mediante integración en $\varpi$;
- gráfica de $\epsilon_{N_F}$ frente a $N_F$;
- gráfica de $|P_n|$ y del cociente de borde;
- tabla de condicionamiento de $\mathsf L_{N_F}$.

---

## 2. Registro de verificaciones reproducibles

### Verificación V-001 — Suite actual

**Último resultado conocido antes de crear esta bitácora:** 21 pruebas aprobadas.

Las pruebas cubren:

- propagador y causalidad;
- periodicidad conjunta;
- función de Green estacionaria;
- monodromía y Liouville;
- estabilidad y referencia de Mathieu;
- balance de energía;
- compatibilidad del LaTeX Markdown con GitHub.

El comando reproducible es

```powershell
.\.venv\Scripts\python.exe -m pytest
```

### Verificación V-002 — Compatibilidad matemática con GitHub

No se empleará el macro genérico de nombres de operador que GitHub bloquea. Se
usarán, según corresponda,

```math
\mathrm{tr},
\qquad
\mathrm{Re},
\qquad
\mathrm{Im},
\qquad
\mathrm{diag}.
```

La prueba `tests/test_markdown_math.py` revisa la bitácora automáticamente porque
está dentro de `docs/`.

### Verificación V-003 — Cierre de la primera entrega

**Fecha:** 11-08-2026

**Commit base:** `56d2b2e091e7` en la rama `codex/marco-teorico`; la bitácora aún
no estaba confirmada al ejecutar esta verificación.

**Entorno:** Python 3.13.6, pytest 9.1.1.

Se ejecutó

```powershell
.\.venv\Scripts\python.exe -m pytest
```

y se obtuvieron $21$ pruebas aprobadas en $1.52\ \mathrm{s}$. También se ejecutó

```powershell
.\.venv\Scripts\python.exe -m ruff check src tests
```

sin observaciones. La auditoría estática de esta versión contó $570$ delimitadores
dobles de bloque, $23$ aperturas y $23$ cierres de entornos LaTeX, y encontró cero
caracteres de control, cero líneas con espacios finales y cero usos del macro
rechazado por GitHub.

### Verificación V-004 — Preservación de LaTeX frente a CommonMark

**Fecha:** 11-08-2026

La API de Markdown de GitHub confirmó que los delimitadores dobles permiten que
CommonMark consuma una barra de un salto de fila LaTeX y también las barras de
ciertos comandos de espaciado. Por ello, las $570$ ecuaciones de bloque del proyecto
se migraron a fences `math`, que entregan el contenido LaTeX intacto a MathJax.

Las expresiones inline que contienen escapes sensibles se escriben con la forma
protegida oficial de GitHub. Las pruebas automáticas ahora rechazan nuevos bloques
con delimitadores dobles, fences sin cierre, bloques matemáticos vacíos y escapes
inline vulnerables al preprocesado de CommonMark.

---

## 3. Decisiones, correcciones y advertencias

### D-001 — Periodos

En esta bitácora se separan

```math
T_m=\frac{2\pi}{\Omega_m}
```

y

```math
T_\tau=\omega_0T_m=\frac{2\pi}{\nu}.
```

### D-002 — Núcleo y tasa de crecimiento

Se reserva $g(\tau,s)$ para la función de Green. Las tasas de Floquet se escribirán
como

```math
\Gamma_j=\frac{\log|\lambda_j|}{T_\tau}.
```

### D-003 — Disipación

En el código actual

```math
W_{\mathrm{dis}}
=\int_0^\tau-2\zeta v^2\,ds
\le0.
```

Si en una etapa posterior se desea expresar la pérdida como cantidad positiva,
usaremos

```math
W_{\mathrm{loss}}
=\int_0^\tau2\zeta v^2\,ds
\ge0,
```

y entonces

```math
\Delta\mathcal E
=-W_{\mathrm{loss}}
+W_{\mathrm{mod}}
+W_{\mathrm{in}}.
```

### D-004 — Qué todavía no está demostrado

No se registrarán como resultados alcanzados:

- la convergencia tiempo–Floquet;
- una tasa exponencial de truncamiento;
- el modelo Maxwell espacial;
- la covarianza de ruido ciclostacionario;
- la capacidad del canal;
- el costo físico completo del actuador.

Esos puntos pertenecen al programa de investigación, no a los resultados actuales.

### D-005 — Correcciones de la auditoría matemática inicial

**Estado:** [CORREGIDO] el 11-08-2026 antes de publicar esta hoja.

La primera revisión cruzada dejó registradas cinco precisiones:

1. $\nu=2$ es el centro de la aproximación resonante de primer orden, no un centro
   exacto con amortiguamiento finito.
2. En el benchmark inestable es positivo el trabajo neto final
   $W_{\mathrm{mod}}(\tau_f)$; ni el trabajo acumulado ni su derivada tienen que ser
   positivos en cada instante.
3. $P_n=0$ fuera de $|n|\le N_F$ es una extensión de la aproximación de Galerkin,
   no una afirmación sobre la solución infinita exacta.
4. La convergencia cuando $N_F$ crece no tiene que ser monótona paso a paso.
5. Toda comparación tiempo–Floquet usará la misma entrada y la misma historia, o
   cuantificará explícitamente el transitorio omitido.

---

## 4. Plantilla para la próxima hoja

```markdown
## Hoja M-XXX — Título

**Fecha:** DD-MM-AAAA
**Estado:** [PENDIENTE], [DERIVADO], [VERIFICADO], [HIPÓTESIS] o [CORREGIDO]
**Depende de:** M-___
**Código relacionado:** ruta del archivo
**Prueba relacionada:** nombre de la prueba

### Problema

¿Qué se quiere calcular o demostrar?

### Datos e hipótesis

Escribir todos los parámetros, unidades, convenciones y condiciones iniciales.

### Desarrollo paso a paso

No omitir cambios de índice, signos, factores de $2\pi$ ni términos de frontera.

### Comprobación independiente

Incluir al menos una de estas pruebas: sustitución inversa, caso límite, identidad
exacta, comparación numérica o segunda representación.

### Resultado

Encerrar únicamente lo que realmente quedó demostrado.

### Pendiente

Registrar explícitamente qué falta y cuál será la siguiente hoja.
```

---

## 5. Próxima entrada prevista

La siguiente hoja se abrirá al implementar la matriz $\mathsf L_{N_F}(\varpi)$.
Deberá registrar:

1. orden exacto de los índices;
2. estructura de diagonales;
3. condicionamiento;
4. solución para $m=0$;
5. primera comparación con integración temporal;
6. cualquier error de fase encontrado durante la implementación.
