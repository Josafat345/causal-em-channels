# Marco teórico: canales electromagnéticos causales espacio-temporales

> **Estado de la revisión:** 10 de agosto de 2026
>
> **Objetivo:** construir la base matemática y física necesaria para investigar
> canales electromagnéticos dispersivos y modulados en espacio y tiempo, con
> causalidad, energía, estabilidad, ruido y capacidad tratados dentro de un mismo
> modelo.

## 0. Cómo estudiar este documento

Este capítulo no debe leerse como una colección de fórmulas aisladas. La cadena
lógica que seguiremos es

```math
\text{Maxwell}
\longrightarrow
\text{respuesta material causal}
\longrightarrow
\text{sistema dinámico}
\longrightarrow
\text{Floquet}
\longrightarrow
\text{energía y ruido}
\longrightarrow
\text{canal y capacidad}.
```

El orden importa. Una matriz de transferencia armónica puede ser algebraicamente
correcta y, aun así, describir un medio no causal, una amplificación sin fuente de
energía o un estado paramétricamente inestable. Del mismo modo, una fórmula de
Shannon puede ser correcta para una matriz dada, pero físicamente irrelevante si
esa matriz no procede de un problema de Maxwell con puertos, ruido y recursos bien
definidos.

Al terminar el documento deberías poder responder, sin recurrir a analogías vagas,
las siguientes preguntas:

1. ¿Qué significa causalidad cuando el medio depende de dos tiempos $t$ y $t'$?
2. ¿Por qué una permitividad instantánea $\varepsilon(t)$ no basta para representar
   un material dispersivo?
3. ¿Cómo aparecen las bandas laterales $\omega+n\Omega_m$?
4. ¿Cómo se decide si una modulación periódica es estable?
5. ¿De dónde procede la energía de una onda amplificada paramétricamente?
6. ¿Cuándo un sistema temporal es realmente no recíproco?
7. ¿Cómo se construye el ruido compatible con la disipación material?
8. ¿Cuál es el objeto matemático al que debe aplicarse la capacidad de Shannon?
9. ¿Qué parte de nuestra propuesta ya existe y dónde puede haber una contribución
   original verificable?

### Mapa de lectura

- **Base física y matemática:** secciones 1–7.
- **Modulación, interfaces, Floquet, energía y reciprocidad:** secciones 8–12.
- **Ruido, canal, capacidad y límites físicos:** secciones 13–16.
- **Estado del arte y dirección original:** secciones 17–20.
- **Método de trabajo, diagnóstico y plan de nivelación:** secciones 21–26.

Para una primera lectura, estudia 1–12 y 17–19. Después realiza el diagnóstico de
la sección 22 y vuelve a 13–16 cuando tengas firmes procesos aleatorios e
información.

## 1. Alcance y pregunta de investigación

### 1.1 Objeto físico

Consideramos una región electromagnética que puede contener materiales
dispersivos, pérdidas, modulación temporal y periodicidad espacial. Fuentes
controlables excitan la región y receptores observan combinaciones de los campos.
De forma abstracta,

```math
\mathbf y(t)
=\int_{-\infty}^{t}
\mathcal H(t,t')\mathbf x(t')\,dt'
+\mathbf n(t),
```

donde $\mathbf x$ representa señales de entrada físicamente normalizadas,
$\mathbf y$ representa observaciones de salida, $\mathcal H(t,t')$ es un operador
causal de dos tiempos y $\mathbf n$ es ruido. Si la modulación tiene periodo $T_m$,

```math
\mathcal H(t+T_m,t'+T_m)=\mathcal H(t,t').
```

La periodicidad correcta es conjunta: desplazar ambos tiempos un periodo no cambia
el experimento. En general no se cumple
$\mathcal H(t,t')=\mathcal H(t-t')$; esa reducción corresponde únicamente a un
sistema invariante en el tiempo.

### 1.2 Pregunta central

Una formulación concreta para el proyecto es:

> ¿Cuál es la tasa máxima de información transferible entre puertos de un sistema
> electromagnético lineal, dispersivo y periódicamente modulado, cuando se imponen
> simultáneamente causalidad, estabilidad de Floquet, ruido físicamente consistente,
> potencia de señal, trabajo de bombeo y geometría finita?

Esta pregunta no supone que la modulación mejore necesariamente la capacidad. El
resultado puede ser una mejora, una redistribución espectral, una pérdida neta o
un límite superior que demuestre que cierta ventaja aparente desaparece al contar
el bombeo y el ruido.

### 1.3 Lo que no se supondrá

No supondremos sin demostración que:

- $\varepsilon(t)$ es una descripción suficiente de un material real;
- conversión de frecuencia equivale a ganancia;
- asimetría de transmisión equivale a no reciprocidad;
- $\rho(M)>1$ constituye un canal estacionario utilizable;
- cada banda lateral crea un nuevo grado de libertad físico independiente;
- una pérdida $\gamma$ puede añadirse sin introducir fluctuaciones;
- el bombeo temporal es gratuito.

## 2. Convenciones, notación y prerrequisitos

### 2.1 Convención de Fourier

Usaremos

```math
\widehat f(\omega)
=\int_{-\infty}^{\infty}f(t)e^{\mathrm{i}\omega t}\,dt,
\qquad
f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}
\widehat f(\omega)e^{-\mathrm{i}\omega t}\,d\omega.
```

Por tanto, un fasor positivo evoluciona como $e^{-\mathrm{i}\omega t}$. Con esta
convención, una respuesta causal estable es analítica en el semiplano
$`\mathrm{Im}\,\omega>0`$, y un material pasivo ordinario satisface
$`\mathrm{Im}\,\chi(\omega)\ge 0`$ para $\omega>0$.

### 2.2 Símbolos principales

| Símbolo | Significado |
|---|---|
| $\mathbf E,\mathbf H$ | campos eléctrico y magnético |
| $\mathbf D,\mathbf B$ | desplazamiento eléctrico e inducción magnética |
| $\mathbf P,\mathbf M$ | polarización y magnetización |
| $\rho_f,\mathbf J_f$ | carga y corriente libres |
| $\chi$ | susceptibilidad material |
| $T_m,\Omega_m$ | periodo y frecuencia angular de modulación, $T_m=2\pi/\Omega_m$ |
| $T_{\mathrm b}$ | temperatura absoluta de un baño térmico |
| $U(t,s)$ | propagador desde $s$ hasta $t$ |
| $M$ | matriz u operador monodrómico |
| $\lambda_j,\mu_j$ | multiplicadores y exponentes de Floquet |
| $\mathsf H(\omega)$ | matriz de transferencia armónica levantada |
| $\mathbf Q$ | covarianza de entrada |
| $\mathbf K_n$ | covarianza de ruido |

Los símbolos en negrita minúscula representan vectores finitos; las mayúsculas
caligráficas representan operadores que pueden actuar sobre campos. El superíndice
$\dagger$ es el adjunto hermítico y $\mathsf T$ la transposición sin conjugación.

### 2.3 Prerrequisitos mínimos

Para trabajar con solvencia se necesitan cuatro niveles:

1. **Ingeniería:** fasores, potencia compleja, líneas de transmisión, parámetros
   $S$, ruido térmico y modulación.
2. **Física:** Maxwell, condiciones de frontera, dispersión, oscilador de Lorentz,
   teorema de Poynting y termodinámica lineal.
3. **Matemática:** álgebra lineal compleja, EDO, transformadas de Fourier y Laplace,
   variable compleja, distribuciones, operadores y optimización convexa.
4. **Probabilidad e información:** procesos gaussianos, covarianzas espectrales,
   entropía diferencial, información mutua y canales MIMO.

La ruta de nivelación de la sección 22 permite detectar y subsanar huecos sin
detener el proyecto completo.

## 3. Electrodinámica macroscópica

### 3.1 Ecuaciones de Maxwell

En unidades SI,

```math
\nabla\times\mathbf E(\mathbf r,t)
=-\frac{\partial\mathbf B(\mathbf r,t)}{\partial t},
```

```math
\nabla\times\mathbf H(\mathbf r,t)
=\mathbf J_f(\mathbf r,t)
+\frac{\partial\mathbf D(\mathbf r,t)}{\partial t},
```

```math
\nabla\cdot\mathbf D(\mathbf r,t)=\rho_f(\mathbf r,t),
\qquad
\nabla\cdot\mathbf B(\mathbf r,t)=0.
```

La divergencia de la ley de Ampère–Maxwell proporciona la ecuación de continuidad,

```math
\frac{\partial\rho_f}{\partial t}+\nabla\cdot\mathbf J_f=0.
```

Las ecuaciones de Maxwell no cierran el problema por sí solas. Deben especificarse
las relaciones constitutivas, las condiciones iniciales, las fronteras y la forma
en que se excita y observa el sistema.

### 3.2 Separación entre campo y materia

Para un medio no magnético simple,

```math
\mathbf D=\varepsilon_0\mathbf E+\mathbf P,
\qquad
\mathbf B=\mu_0\mathbf H.
```

En un medio magnetodieléctrico,

```math
\mathbf D=\varepsilon_0\mathbf E+\mathbf P,
\qquad
\mathbf B=\mu_0(\mathbf H+\mathbf M).
```

La polarización y la magnetización no son parámetros auxiliares: contienen los
grados de libertad materiales que almacenan energía, disipan y producen memoria.
Eliminar esos estados demasiado pronto puede ocultar la causalidad y el trabajo de
modulación.

### 3.3 Forma operatorial de Maxwell

Agrupando los campos en

```math
\mathbf F=
\begin{pmatrix}
\mathbf E\\
\mathbf H
\end{pmatrix},
```

una discretización espacial compatible para un medio instantáneo puede escribirse
como

```math
\frac{d}{dt}[\mathcal M(t)\mathbf F(t)]
=\mathcal C\mathbf F(t)+\mathbf s(t),
```

donde $\mathcal C$ representa los rotacionales discretos, $\mathcal M$ contiene la
respuesta constitutiva instantánea cuando esta existe y $\mathbf s$ reúne las
fuentes. Al expandir la derivada aparece explícitamente

```math
\mathcal M(t)\dot{\mathbf F}(t)
=\left[\mathcal C-\dot{\mathcal M}(t)\right]\mathbf F(t)
+\mathbf s(t).
```

Para medios dispersivos esta forma debe ampliarse con estados materiales; no basta
con reemplazar $\mathcal M$ por una matriz dependiente de $\omega$ dentro de una
simulación temporal.

### 3.4 Condiciones de frontera espaciales

En una interfaz espacial ordinaria con normal $\widehat{\mathbf n}$,

```math
\widehat{\mathbf n}\times(\mathbf E_2-\mathbf E_1)=\mathbf 0,
\qquad
\widehat{\mathbf n}\times(\mathbf H_2-\mathbf H_1)=\mathbf K_f,
```

```math
\widehat{\mathbf n}\cdot(\mathbf D_2-\mathbf D_1)=\sigma_f,
\qquad
\widehat{\mathbf n}\cdot(\mathbf B_2-\mathbf B_1)=0.
```

Estas condiciones proceden de integrar Maxwell sobre la geometría de la interfaz.
No deben trasladarse mecánicamente a una discontinuidad temporal; en la sección 9
veremos que el mecanismo microscópico del cambio temporal determina qué cantidades
pueden presentar impulsos o permanecer continuas.

## 4. Respuesta material, memoria y dispersión

### 4.1 Relación constitutiva lineal más general

Una respuesta electromagnética lineal, bianisótropa y espacialmente no local puede
escribirse como

```math
\begin{pmatrix}
\mathbf P\\
\mu_0\mathbf M
\end{pmatrix}(\mathbf r,t)
=\int_{\mathbb R^3}\!d^3\mathbf r'
\int_{-\infty}^{\infty}\!dt'\,
\boldsymbol{\mathcal K}(\mathbf r,\mathbf r';t,t')
\begin{pmatrix}
\mathbf E\\
\mathbf H
\end{pmatrix}(\mathbf r',t').
```

El núcleo matricial puede contener bloques eléctricos, magnéticos y
magnetoeléctricos,

```math
\boldsymbol{\mathcal K}=
\begin{pmatrix}
\boldsymbol{\mathcal K}_{ee}&\boldsymbol{\mathcal K}_{em}\\
\boldsymbol{\mathcal K}_{me}&\boldsymbol{\mathcal K}_{mm}
\end{pmatrix}.
```

Este núcleo es dimensional: sus cuatro bloques no tienen necesariamente las mismas
unidades. Reservaremos $\boldsymbol\chi_e$ para la susceptibilidad eléctrica
adimensional definida mediante un factor explícito $\varepsilon_0$.

La localidad espacial es una aproximación adicional,

```math
\boldsymbol{\mathcal K}(\mathbf r,\mathbf r';t,t')
=\boldsymbol{\mathcal K}(\mathbf r;t,t')
\delta(\mathbf r-\mathbf r').
```

En este proyecto comenzaremos con localidad espacial, pero mantendremos explícita
la memoria temporal.

### 4.2 Medio invariante en el tiempo

Si el material está en equilibrio y no cambia en el tiempo,

```math
\boldsymbol{\chi}(t,t')=\boldsymbol{\chi}(t-t').
```

Definiendo el retardo $\tau=t-t'$,

```math
\mathbf P(t)
=\varepsilon_0\int_0^{\infty}
\boldsymbol{\chi}_e(\tau)\mathbf E(t-\tau)\,d\tau,
```

y en frecuencia

```math
\widehat{\mathbf P}(\omega)
=\varepsilon_0\boldsymbol{\chi}_e(\omega)
\widehat{\mathbf E}(\omega),
\qquad
\boldsymbol{\varepsilon}(\omega)
=\varepsilon_0\left[\mathbf I+\boldsymbol{\chi}_e(\omega)\right].
```

La dispersión es precisamente la dependencia con $\omega$ producida por la
memoria. Una constante real $\varepsilon$ es una aproximación válida solo en una
ventana donde la respuesta cambia poco y las pérdidas son despreciables.

### 4.3 Oscilador de Lorentz

El modelo material mínimo para una resonancia es

```math
\ddot{\mathbf P}
+\gamma\dot{\mathbf P}
+\omega_0^2\mathbf P
=\varepsilon_0\omega_p^2\mathbf E.
```

Para una excitación proporcional a $e^{-\mathrm{i}\omega t}$,

```math
\boldsymbol{\chi}_L(\omega)
=\frac{\omega_p^2}
{\omega_0^2-\omega^2-\mathrm{i}\gamma\omega}.
```

Si $\gamma>0$ y $\omega_0>0$, sus polos se encuentran estrictamente en el
semiplano inferior y, para $\omega>0$,

```math
\mathrm{Im}\,\chi_L(\omega)
=\frac{\omega_p^2\gamma\omega}
{(\omega_0^2-\omega^2)^2+\gamma^2\omega^2}
\ge 0.
```

Una suma de resonancias permite ajustar materiales reales,

```math
\chi(\omega)=\sum_{j=1}^{N_r}
\frac{f_j\omega_{p,j}^2}
{\omega_{0,j}^2-\omega^2-\mathrm{i}\gamma_j\omega}.
```

El modelo de Drude es el caso $\omega_0=0$,

```math
\chi_D(\omega)
=-\frac{\omega_p^2}{\omega^2+\mathrm{i}\gamma\omega}.
```

La susceptibilidad de polarización de Drude tiene polos en
$\omega=0$ y $\omega=-\mathrm i\gamma$. Por ello la polarización libre no es BIBO
estable ante una componente continua; la corriente y la conductividad sí poseen una
respuesta estacionaria. El polo en el origen requiere un límite causal o tratamiento
distribucional al aplicar relaciones de dispersión.

### 4.4 Por qué no basta con $\varepsilon(t)$

La escritura

```math
\mathbf D(t)=\varepsilon(t)\mathbf E(t)
```

supone respuesta instantánea. Puede ser útil para un dieléctrico aproximadamente
no dispersivo, pero cerca de una resonancia omite los estados materiales. Una
modulación rápida puede cambiar la dinámica microscópica y no solo el valor de un
parámetro estático. Un modelo más seguro es

```math
\ddot{\mathbf P}
+\gamma(t)\dot{\mathbf P}
+\omega_0^2(t)\mathbf P
=\varepsilon_0\omega_p^2(t)\mathbf E+\boldsymbol\xi(t),
```

acompañado de una explicación física de qué controla cada coeficiente. La literatura
reciente ha mostrado que la dispersión y el mecanismo de conmutación cambian tanto
las condiciones temporales como el balance de energía
([Solís, Kastner y Engheta, 2021](https://doi.org/10.1364/PRJ.427368);
[Sloan et al., 2024](https://doi.org/10.1021/acsphotonics.3c00773);
[Galiffi et al., 2025](https://doi.org/10.1038/s41377-025-01947-2)).

## 5. Causalidad, analiticidad y Kramers–Kronig

### 5.1 Causalidad en el dominio temporal

La causalidad de la respuesta lineal exige

```math
\boldsymbol{\mathcal K}(\mathbf r,\mathbf r';t,t')=\mathbf 0
\qquad\text{si}\qquad t<t'.
```

Equivale a afirmar que la salida presente no depende de una entrada futura. En un
medio LTI,

```math
\boldsymbol{\chi}(\tau)=\mathbf 0
\qquad\text{para}\qquad \tau<0.
```

La causalidad no es lo mismo que estabilidad. Por ejemplo, el núcleo

```math
h(t)=e^{at}H(t),\qquad a>0,
```

es causal, pero su respuesta crece y no es BIBO estable.

### 5.2 Analiticidad

Para una respuesta causal y BIBO estable, por ejemplo
$\chi\in L^1(0,\infty)$,

```math
\chi(\omega)
=\int_0^\infty\chi(\tau)e^{\mathrm{i}\omega\tau}\,d\tau
```

converge y es analítica cuando $`\mathrm{Im}\,\omega>0`$. Si la respuesta crece
como $e^{at}$, la integral converge inicialmente solo para
$`\mathrm{Im}\,\omega>a`$; las respuestas no integrables deben tratarse mediante
una transformada Fourier–Laplace y valores frontera distribucionales. La
analiticidad, junto con el comportamiento asintótico apropiado, conduce a relaciones
de dispersión.

### 5.3 Relaciones de Kramers–Kronig

Para una susceptibilidad escalar que tiende a cero con suficiente rapidez,

```math
\mathrm{Re}\,\chi(\omega)
=\frac{1}{\pi}\mathcal P
\int_{-\infty}^{\infty}
\frac{\mathrm{Im}\,\chi(\omega')}
{\omega'-\omega}\,d\omega',
```

```math
\mathrm{Im}\,\chi(\omega)
=-\frac{1}{\pi}\mathcal P
\int_{-\infty}^{\infty}
\frac{\mathrm{Re}\,\chi(\omega')}
{\omega'-\omega}\,d\omega'.
```

Para una respuesta real en el tiempo,

```math
\chi(-\omega)=\chi(\omega)^*,
```

y las relaciones pueden escribirse para $\omega>0$ como

```math
\mathrm{Re}\,\chi(\omega)
=\frac{2}{\pi}\mathcal P
\int_0^\infty
\frac{\omega'\,\mathrm{Im}\,\chi(\omega')}
{\omega'^2-\omega^2}\,d\omega',
```

```math
\mathrm{Im}\,\chi(\omega)
=-\frac{2\omega}{\pi}\mathcal P
\int_0^\infty
\frac{\mathrm{Re}\,\chi(\omega')}
{\omega'^2-\omega^2}\,d\omega'.
```

Si $\chi$ no desaparece en alta frecuencia, se deben usar relaciones sustraídas.
Kramers–Kronig no es una receta para extrapolar datos arbitrarios: requiere
causalidad, analiticidad, simetría de realidad y condiciones asintóticas compatibles.

### 5.4 Pasividad y funciones de Herglotz

En un medio LTI pasivo, el trabajo acumulado que el campo entrega al material no
puede ser negativo para una excitación que parte del reposo. En una formulación
eléctrica simple,

```math
W_{\mathrm{mat}}(t)
=\int_{-\infty}^{t}
\mathbf E(\tau)\cdot\dot{\mathbf P}(\tau)\,d\tau
\ge 0.
```

En frecuencia, la combinación adecuada de la susceptibilidad constituye una
función matricial de Herglotz: es analítica en el semiplano superior y su parte
imaginaria es semidefinida positiva. Esta estructura produce positividad de energía,
reglas de suma y límites de propagación. Bajo hipótesis lineales generales, la
pasividad es suficiente para garantizar causalidad
([Welters, Avniel y Johnson, 2014](https://doi.org/10.1103/PhysRevA.90.023847)).

La implicación inversa no es cierta: un sistema puede ser causal y activo.

### 5.5 Qué cambia en un medio dependiente del tiempo

En un medio LTV no existe, en general, una única función escalar $\chi(\omega)$.
Se debe conservar el núcleo de dos tiempos o una susceptibilidad de dos frecuencias,

```math
\widehat{\mathbf P}(\omega)
=\varepsilon_0\int_{-\infty}^{\infty}
\frac{d\omega'}{2\pi}\,
\boldsymbol{\chi}(\omega,\omega')
\widehat{\mathbf E}(\omega').
```

La causalidad sigue actuando sobre el retardo positivo. Definiendo

```math
\mathbf c(t,\tau)=\boldsymbol\chi(t,t-\tau),
\qquad
\mathbf c(t,\tau)=\mathbf0\quad\text{para }\tau<0,
```

la transformada causal

```math
\mathbf C(t,z)=\int_0^\infty
\mathbf c(t,\tau)e^{\mathrm iz\tau}\,d\tau
```

es el objeto sobre cuya frecuencia $z$, para $t$ fijo, actúan las relaciones de
Hilbert. En un medio periódico también pueden aplicarse a cada
$\mathbf H_n(z)$ bajo las hipótesis de regularidad. No se imponen independientemente
en ambos argumentos de $\boldsymbol\chi(\omega,\omega')$ ni a una "permitividad
instantánea". Además, fuera del equilibrio,
$`\mathrm{Im}\,\chi`$ ya no puede interpretarse por sí sola como absorción total,
porque existe transferencia de energía entre la señal y el accionamiento externo.
Una derivación microscópica moderna de esta respuesta se encuentra en
[Sloan et al. (2024)](https://doi.org/10.1021/acsphotonics.3c00773).

### 5.6 Pruebas computacionales de causalidad

Un modelo numérico deberá superar, como mínimo:

1. **Soporte temporal:** $`\|\mathcal H(t,t')\|`$ debe ser cero, dentro de tolerancia,
   para $t<t'$.
2. **Composición:** $U(t,s)=U(t,u)U(u,s)$ para $t\ge u\ge s$.
3. **Analiticidad:** los polos de un modelo LTI racional y exponencialmente estable
   deben satisfacer $`\mathrm{Im}\,\omega_p<0`$ con nuestra convención; los polos
   reales de límites ideales requieren un tratamiento separado.
4. **Kramers–Kronig:** las partes real e imaginaria deben reconstruirse dentro de
   una banda interior, controlando truncamiento y colas espectrales.
5. **Límite estacionario:** al apagar la modulación, el núcleo de dos tiempos debe
   reducirse a una función del retardo.

## 6. Sistemas lineales variables en el tiempo

### 6.1 Núcleo de dos tiempos

La representación causal más útil para un sistema lineal variable en el tiempo es

```math
\mathbf y(t)=\int_0^\infty
\mathbf h(t,\tau)\mathbf x(t-\tau)\,d\tau,
```

donde $\tau$ es el retardo y

```math
\mathbf h(t,\tau)=\mathbf 0
\qquad\text{para}\qquad \tau<0.
```

La forma equivalente en los dos instantes es

```math
\mathcal H(t,t')=\mathbf h(t,t-t')H(t-t').
```

Para un sistema periódicamente variable en el tiempo, o LPTV,

```math
\mathbf h(t+T_m,\tau)=\mathbf h(t,\tau),
```

lo cual equivale a

```math
\mathcal H(t+T_m,t'+T_m)=\mathcal H(t,t').
```

Esta representación fue anticipada en la teoría de redes variables de Zadeh, que
introdujo funciones de sistema dependientes del tiempo y de dos frecuencias
([Zadeh, 1950](https://doi.org/10.1109/JRPROC.1950.231083)).

### 6.2 Expansión armónica

La periodicidad permite desarrollar

```math
\mathbf h(t,\tau)
=\sum_{n\in\mathbb Z}
\mathbf h_n(\tau)e^{-\mathrm{i}n\Omega_m t},
\qquad
\Omega_m=\frac{2\pi}{T_m}.
```

Si la entrada es monocromática,

```math
\mathbf x(t)=\mathbf X e^{-\mathrm{i}\omega t},
```

entonces

```math
\mathbf y(t)=\sum_{n\in\mathbb Z}
\mathbf H_n(\omega)\mathbf X
e^{-\mathrm{i}(\omega+n\Omega_m)t},
```

con

```math
\mathbf H_n(\omega)
=\int_0^\infty
\mathbf h_n(\tau)e^{\mathrm{i}\omega\tau}\,d\tau.
```

Por tanto, la salida contiene bandas laterales en

```math
\omega_n=\omega+n\Omega_m.
```

No se trata de una no linealidad respecto a la señal: para una modulación prescrita,
el sistema sigue siendo lineal en $\mathbf x$. La fuente de conversión es la
dependencia temporal de sus coeficientes.

### 6.3 Susceptibilidad de dos frecuencias

Para una modulación periódica, la susceptibilidad tiene soporte sobre líneas
separadas por $\Omega_m$,

```math
\boldsymbol{\chi}(\omega,\omega')
=2\pi\sum_{n\in\mathbb Z}
\boldsymbol{\chi}_n(\omega')
\delta(\omega-\omega'-n\Omega_m).
```

Así,

```math
\widehat{\mathbf P}(\omega+n\Omega_m)
=\varepsilon_0
\boldsymbol{\chi}_n(\omega)
\widehat{\mathbf E}(\omega)
```

para una única componente de entrada. En el problema general, cada banda lateral de
entrada contribuye a todas las de salida y el operador se convierte en una matriz
infinita.

### 6.4 Sistemas lentos y canales subdispersivos

En telecomunicaciones también se emplea la función de dispersión
$S_H(\tau,\nu_D)$ de un canal LTV, donde $\tau$ es retardo y $\nu_D$ desplazamiento
Doppler. Un canal se llama aproximadamente *underspread* cuando su soporte ocupa un
área pequeña en el plano retardo–Doppler. Esa aproximación facilita una descripción
local tiempo–frecuencia, pero no debe confundirse con nuestro caso LPTV: una
modulación determinista rápida puede estar bien descrita por Floquet aunque no sea
"lenta" respecto de la portadora.

## 7. Forma de estado, propagadores y funciones de Green

### 7.1 Realización finita

Un medio dispersivo representado mediante ecuaciones diferenciales auxiliares puede
escribirse como

```math
\dot{\mathbf z}(t)
=\mathbf A(t)\mathbf z(t)
+\mathbf B(t)\mathbf u(t)
+\mathbf G(t)\boldsymbol\eta(t),
```

```math
\mathbf y(t)
=\mathbf C(t)\mathbf z(t)
+\mathbf D(t)\mathbf u(t).
```

El estado $\mathbf z$ puede contener muestras de $\mathbf E$ y $\mathbf H$, además
de $\mathbf P_j$, $\dot{\mathbf P}_j$ y otros grados de libertad materiales. Esta
realización conserva la memoria sin utilizar una convolución completa en cada paso
temporal.

### 7.2 Propagador

El propagador homogéneo satisface

```math
\frac{\partial}{\partial t}\mathbf U(t,s)
=\mathbf A(t)\mathbf U(t,s),
\qquad
\mathbf U(s,s)=\mathbf I.
```

Formalmente,

```math
\mathbf U(t,s)
=\mathcal T
\exp\left(\int_s^t\mathbf A(\tau)\,d\tau\right),
```

donde $\mathcal T$ ordena temporalmente los factores. Si
$[\mathbf A(t_1),\mathbf A(t_2)]\ne\mathbf 0$, no es válido reemplazar esta
expresión por la exponencial de la integral ordinaria sin ordenamiento.

El propagador cumple

```math
\mathbf U(t,s)=\mathbf U(t,u)\mathbf U(u,s),
\qquad t\ge u\ge s.
```

### 7.3 Fórmula de Duhamel

La solución es

```math
\mathbf z(t)
=\mathbf U(t,t_0)\mathbf z(t_0)
+\int_{t_0}^{t}
\mathbf U(t,s)\mathbf B(s)\mathbf u(s)\,ds
+\int_{t_0}^{t}
\mathbf U(t,s)\mathbf G(s)\boldsymbol\eta(s)\,ds.
```

Por tanto, el núcleo entrada–salida es

```math
\mathcal H(t,s)
=\mathbf C(t)\mathbf U(t,s)\mathbf B(s)H(t-s)
+\mathbf D(t)\delta(t-s).
```

Esta ecuación conecta de forma exacta la dinámica física con el canal causal.

### 7.4 Operadores de Maxwell

Después de discretizar el espacio, la misma estructura se aplica a Maxwell. En el
límite continuo, $\mathbf A(t)$ se reemplaza por un operador diferencial
$\mathcal A(t)$ y deben especificarse su dominio y las condiciones de frontera.
Esto introduce sutilezas ausentes en una matriz finita: espectro continuo,
resonancias radiativas, operadores no normales y posibles dominios dependientes del
tiempo.

### 7.5 Función de Green electromagnética

Para una corriente eléctrica fuente,

```math
\mathbf E(\mathbf r,t)
=\int d^3\mathbf r'
\int_{-\infty}^{t}dt'\,
\boldsymbol{\mathcal G}_{EJ}
(\mathbf r,\mathbf r';t,t')
\mathbf J(\mathbf r',t').
```

En un medio LTI homogéneo, la función depende de
$\mathbf r-\mathbf r'$ y $t-t'$. En un medio espacio-temporal general depende de
los cuatro argumentos. Esta función de Green es el objeto natural para conectar
volúmenes transmisores y receptores antes de elegir antenas o modos específicos.

## 8. Modulación temporal y espacio-temporal

### 8.1 Parámetros modulados

Una modulación periódica escalar típica es

```math
a(t)=a_0+\sum_{n\ne0}a_n e^{-\mathrm{i}n\Omega_m t},
\qquad
a_{-n}=a_n^*
```

para que $a(t)$ sea real. En el espacio,

```math
a(\mathbf r,t)
=\sum_{\mathbf G,n}
a_{\mathbf G,n}
e^{\mathrm{i}\mathbf G\cdot\mathbf r}
e^{-\mathrm{i}n\Omega_m t}.
```

Una componente con vector de modulación $\mathbf K$ y frecuencia $\Omega_m$ acopla

```math
(\mathbf k,\omega)
\longrightarrow
(\mathbf k+\mathbf K,\omega+\Omega_m).
```

En lenguaje cuántico, el intercambio elemental con el bombeo corresponde a energía
$\hbar\Omega_m$ y momento $\hbar\mathbf K$. En el tratamiento clásico representa
simplemente el intercambio de frecuencia y número de onda impuesto por la
periodicidad.

### 8.2 Modulación puramente temporal

Si el medio es espacialmente uniforme pero cambia en el tiempo, la invariancia por
traslación espacial conserva $\mathbf k$, mientras la frecuencia puede cambiar:

```math
\mathbf k_{\mathrm{después}}=\mathbf k_{\mathrm{antes}},
\qquad
\omega_{\mathrm{después}}\ne\omega_{\mathrm{antes}}.
```

Esta es la dualidad parcial con una frontera espacial, donde la frecuencia se
conserva y cambia la componente normal del vector de onda. Es una dualidad útil,
pero no exacta: el tiempo tiene una orientación causal que el espacio no posee.

### 8.3 Modulación viajera

Una modulación

```math
a(\mathbf r,t)=a_0+\Delta a
\cos(\mathbf K\cdot\mathbf r-\Omega_m t+\phi)
```

selecciona una dirección y una velocidad

```math
v_m=\frac{\Omega_m}{\|\mathbf K\|}.
```

El sesgo de momento puede producir bandas y conversión diferentes para ondas
contrapropagantes. Esta es una ruta común hacia aislamiento sin imanes, pero la
no reciprocidad debe comprobarse con una matriz de dispersión generalizada, no solo
con una gráfica de transmisión en una dirección.

### 8.4 Regímenes de velocidad

En un problema con una sola rama de referencia puede ser útil distinguir

```math
|v_m|<|v_p| \quad\text{subluminal},
```

```math
|v_m|>|v_p| \quad\text{superluminal},
```

y el régimen casi síncrono $|v_m|\approx|v_p|$. Si intervienen dos ramas con
$|v_{p,2}|<|v_{p,1}|$, también puede existir un régimen interluminal,

```math
|v_{p,2}|<|v_m|<|v_{p,1}|.
```

Cerca de sincronismo la interacción acumulada puede ser fuerte y las aproximaciones
perturbativas fallar. En una teoría dispersiva hay que declarar si se compara con
velocidad de fase, de grupo o de frente, y con qué rama material; no basta usar
$c/\sqrt{\varepsilon_r}$.

### 8.5 Evidencia histórica

La propagación en medios temporalmente variables no es una idea reciente. Entre
los antecedentes fundacionales se encuentran la modulación de velocidad de
[Morgenthaler (1958)](https://doi.org/10.1109/TMTT.1958.1124533), las relaciones de
dispersión en medios periódicos espacio-temporales de
[Cassedy y Oliner (1963)](https://doi.org/10.1109/PROC.1963.2566) y el tratamiento
de interfaces temporales dispersivas de
[Fante (1971)](https://doi.org/10.1109/TAP.1971.1139931). La actividad moderna
aporta materiales ultrarrápidos, metasuperficies, circuitos modulados, topología de
Floquet y control experimental que no estaban disponibles en esos trabajos.

## 9. Interfaces temporales

### 9.1 Modelo ideal abrupto

Supongamos que una propiedad material cambia en toda la región en $t=t_0$. Si no
hay corrientes o cargas impulsivas y el modelo constitutivo instantáneo es válido,
integrar Maxwell en un intervalo infinitesimal conduce habitualmente a

```math
\mathbf B(t_0^+)=\mathbf B(t_0^-),
\qquad
\mathbf D(t_0^+)=\mathbf D(t_0^-).
```

La continuidad de $\mathbf E$ o $\mathbf H$ no se sigue en general de esas
hipótesis.

### 9.2 Dependencia del mecanismo físico

La regla anterior no es universal. Si el cambio se produce mediante inyección de
portadores, ionización, conmutación de un capacitor, una corriente externa o un
proceso que genera impulsos, las ecuaciones integradas cambian. En un medio
dispersivo también deben integrarse las ecuaciones de los estados materiales. Para
un oscilador de Lorentz con coeficientes y excitación acotados, sin términos
impulsivos,

```math
[\mathbf P]_{t_0}=\mathbf0,
\qquad
[\dot{\mathbf P}]_{t_0}=\mathbf0.
```

Si la conmutación introduce impulsos, estas continuidades dejan de ser universales:
las condiciones de salto deben obtenerse integrando la ecuación material junto con
los estados del accionamiento.

El trabajo de
[Galiffi et al. (2025)](https://doi.org/10.1038/s41377-025-01947-2) deriva las
condiciones desde el mecanismo microscópico, y
[Ai et al. (2026)](https://doi.org/10.1103/zc87-g67t) compara transiciones de
duración finita bajo distintas condiciones físicas. La lección para este proyecto
es directa: cada salto temporal deberá acompañarse de una ecuación del actuador.

### 9.3 Conmutación finita y límite adiabático

Una transición real tiene duración $\tau_s$. Un parámetro adimensional útil es

```math
\eta_s=\omega_{\mathrm{ref}}\tau_s
=2\pi\frac{\tau_s}{T_{\mathrm{ref}}}.
```

La escala $\omega_{\mathrm{ref}}$ debe declararse: puede ser la frecuencia incidente,
un polo material o la separación instantánea entre modos. Con una elección
apropiada, $\eta_s\ll1$ aproxima una interfaz abrupta y $\eta_s\gg1$ puede permitir
WKB o una aproximación adiabática si no hay cruces ni resonancias. El umbral no es
universal: depende de la trayectoria de parámetros, la dispersión y las condiciones
microscópicas.

## 10. Teoría de Floquet y resonancia paramétrica

### 10.1 Teorema de Floquet

Sea el sistema homogéneo

```math
\dot{\mathbf z}(t)=\mathbf A(t)\mathbf z(t),
\qquad
\mathbf A(t+T_m)=\mathbf A(t).
```

Si $\boldsymbol\Phi(0)=\mathbf I$ es una matriz fundamental, el teorema de
Floquet permite escribir

```math
\boldsymbol\Phi(t)=\mathbf P(t)e^{\mathbf R t},
\qquad
\mathbf P(t+T_m)=\mathbf P(t).
```

La matriz monodrómica es

```math
\mathbf M=\boldsymbol\Phi(T_m).
```

Sus autovalores $\lambda_j$ son los multiplicadores de Floquet. Los exponentes
$\mu_j$ satisfacen

```math
\lambda_j=e^{\mu_jT_m},
\qquad
\mu_j=\frac{1}{T_m}\,\mathrm{Log}\,\lambda_j.
```

El logaritmo es multivaluado:

```math
\mu_j\sim\mu_j+\mathrm{i}n\Omega_m,
\qquad n\in\mathbb Z.
```

Con la convención ondulatoria puede introducirse la cuasifrecuencia

```math
\lambda_j=e^{-\mathrm{i}\omega_{F,j}T_m},
\qquad
\omega_{F,j}=\frac{\mathrm{i}}{T_m}\,\mathrm{Log}\,\lambda_j
\pmod{\Omega_m}.
```

### 10.2 Independencia de la fase inicial

La monodromía calculada desde $t_0$ es

```math
\mathbf M(t_0)=\mathbf U(t_0+T_m,t_0).
```

Para dos fases iniciales,

```math
\mathbf M(t_1)
=\mathbf U(t_1,t_0)\mathbf M(t_0)\mathbf U(t_1,t_0)^{-1}.
```

Por ser matrices semejantes, tienen los mismos multiplicadores. Los autovectores y
la forma de la trayectoria sí dependen de la fase de observación.

### 10.3 Estabilidad

En dimensión finita, la estabilidad exponencial del sistema periódico exige

```math
\rho(\mathbf M)=\max_j|\lambda_j|<1.
```

Si algún $|\lambda_j|>1$, existe crecimiento paramétrico. Si
$|\lambda_j|=1$, se necesita examinar bloques de Jordan, resonancias y la respuesta
forzada; la mera igualdad no garantiza una dinámica acotada.

Además, una matriz no normal puede exhibir crecimiento transitorio grande aun
cuando

```math
\rho(\mathbf M)<1.
```

Por ello conviene medir también la ganancia estroboscópica

```math
G_{N_c}^{\mathrm{estrobo}}
=\max_{0\le k\le N_c}\|\mathbf M^k\|^2,
```

donde $N_c$ es el número de ciclos de modulación observados.

Esta cantidad puede omitir crecimiento dentro del periodo. Una medida física más
completa es

```math
G=\sup_{t\ge s}
\left\|
\mathbf W(t)^{1/2}\mathbf U(t,s)\mathbf W(s)^{-1/2}
\right\|_2^2,
```

donde $\mathbf W(t)$ define una métrica de energía positiva.

### 10.4 Identidad de Liouville

Para un sistema matricial,

```math
\det\mathbf M
=\exp\left(
\int_0^{T_m}\mathrm{tr}\,\mathbf A(t)\,dt
\right).
```

En nuestro oscilador adimensional,

```math
p''+2\zeta p'+[1+m\cos(\nu\tau+\phi)]p=0,
```

se tiene

```math
\det\mathbf M=e^{-2\zeta T_\tau},
\qquad
T_\tau=\frac{2\pi}{\nu}.
```

La condición $|\det\mathbf M|<1$ solo describe contracción de volumen de fase. No
impide que una dirección crezca mientras otra se contrae más.

### 10.5 Reducción a Mathieu

Eliminando el amortiguamiento mediante

```math
p(\tau)=e^{-\zeta\tau}q(\tau)
```

obtenemos

```math
q''+[1-\zeta^2+m\cos(\nu\tau+\phi)]q=0.
```

Con

```math
\theta=\frac{\nu\tau+\phi}{2},
```

la ecuación adopta la forma de Mathieu,

```math
\frac{d^2q}{d\theta^2}
+[a-2q_M\cos(2\theta)]q=0,
```

donde

```math
a=\frac{4(1-\zeta^2)}{\nu^2},
\qquad
q_M=-\frac{2m}{\nu^2}.
```

Para $m$, $\zeta$ y el desajuste $\delta=\nu-2$ pequeños, el promediado da

```math
g_{\pm}
\approx-\zeta
\pm\sqrt{
\left(\frac{m}{4}\right)^2
-\left(\frac{\delta}{2}\right)^2
}.
```

La lengua principal es aproximadamente inestable cuando

```math
\left(\frac{\delta}{2}\right)^2+\zeta^2
<\left(\frac{m}{4}\right)^2.
```

El centro se encuentra más precisamente cerca de
$\nu\simeq2\sqrt{1-\zeta^2}$. En el centro resonante al primer orden, el umbral es

```math
m>4\zeta.
```

Para el benchmark actual,

```math
m=0.20,
\qquad
\zeta=0.02,
```

la estimación produce

```math
g_{\max}\approx-0.02+\frac{0.20}{4}=0.03,
```

en excelente acuerdo con el valor numérico

```math
g_{\max}\approx0.02995.
```

Esto valida el código contra teoría conocida; no es todavía una afirmación de
novedad.

### 10.6 Bloch–Floquet espacio-temporal

Para un medio periódico en espacio y tiempo, un campo puede desarrollarse como

```math
\mathbf F(\mathbf r,t)
=e^{\mathrm{i}(\mathbf k\cdot\mathbf r-\omega_Ft)}
\sum_{\mathbf G,n}
\mathbf F_{\mathbf G,n}
e^{\mathrm{i}\mathbf G\cdot\mathbf r}
e^{-\mathrm{i}n\Omega_m t}.
```

Los armónicos físicos son

```math
\mathbf k_{\mathbf G}=\mathbf k+\mathbf G,
\qquad
\omega_n=\omega_F+n\Omega_m.
```

La pareja $(\mathbf k,\omega_F)$ está definida módulo los vectores recíprocos y
$\Omega_m$. En una periodicidad puramente temporal surgen brechas de momento en
las que la cuasifrecuencia puede adquirir parte imaginaria. En el caso ideal sin
pérdidas y bajo las simetrías simplécticas o seudounitarias correspondientes,
aparecen pares conjugados de amplificación y atenuación; la disipación puede
desplazar ambos exponentes y romper esa simetría simple.

### 10.7 Balance armónico del Lorentz modulado

Para

```math
\ddot P+\gamma\dot P
+\omega_0^2[1+m\cos(\Omega_m t+\phi)]P
=\varepsilon_0\omega_p^2E,
```

introducimos

```math
P(t)=\sum_{n\in\mathbb Z}P_n
e^{-\mathrm{i}(\omega+n\Omega_m)t}.
```

Cada componente satisface

```math
D_n(\omega)P_n
+\frac{m\omega_0^2}{2}
\left(e^{-\mathrm{i}\phi}P_{n-1}
+e^{\mathrm{i}\phi}P_{n+1}\right)
=\varepsilon_0\omega_p^2E_n,
```

con

```math
D_n(\omega)
=\omega_0^2-(\omega+n\Omega_m)^2
-\mathrm{i}\gamma(\omega+n\Omega_m).
```

La matriz es tridiagonal por bloques para una modulación sinusoidal. Una forma de
onda con más armónicos produce más diagonales.

### 10.8 Truncamiento de Floquet

El operador armónico es infinito. Numéricamente se restringe a

```math
-N_F\le n\le N_F.
```

La convergencia no debe darse por supuesta. Deben controlarse, al aumentar $N_F$,

```math
\|\mathsf H^{(N_F+1)}-\mathsf H^{(N_F)}\|,
\qquad
\max_j|\omega_{F,j}^{(N_F+1)}-\omega_{F,j}^{(N_F)}|,
```

```math
|P_{\mathrm{pump}}^{(N_F+1)}-P_{\mathrm{pump}}^{(N_F)}|,
\qquad
|C_{N_F+1}^{\mathrm{Floquet}}-C_{N_F}^{\mathrm{Floquet}}|.
```

Además, después de emparejar ramas y elegirlas de forma consistente módulo
$\Omega_m$, debe comprobarse

```math
e^{-\mathrm i\omega_{F,j}^{(N_F)}T_m}
\longrightarrow\lambda_j(\mathbf M),
```

donde $\mathbf M$ se calcula directamente por evolución temporal y no depende del
truncamiento armónico.

También debe vigilarse la energía que alcanza los armónicos de borde. Las
modulaciones suaves suelen producir decaimiento armónico más rápido; las
conmutaciones abruptas requieren muchos modos. Cerca de un umbral paramétrico o un
punto excepcional, una truncación aparentemente pequeña puede alterar mucho la
respuesta.

## 11. Energía, bombeo, pasividad y ganancia

### 11.1 Teorema de Poynting con polarización

Para

```math
\mathbf D=\varepsilon_0\mathbf E+\mathbf P,
\qquad
\mathbf B=\mu_0\mathbf H,
```

Maxwell produce

```math
\frac{\partial u_{\mathrm{EM}}}{\partial t}
+\nabla\cdot\mathbf S
=-\mathbf E\cdot\mathbf J_f
-\mathbf E\cdot\dot{\mathbf P},
```

donde

```math
u_{\mathrm{EM}}
=\frac{\varepsilon_0}{2}|\mathbf E|^2
+\frac{\mu_0}{2}|\mathbf H|^2,
\qquad
\mathbf S=\mathbf E\times\mathbf H.
```

El término $\mathbf E\cdot\dot{\mathbf P}$ es la potencia transferida del campo
al subsistema material.

### 11.2 Energía del oscilador de Lorentz modulado

Si $\omega_p$ es constante y se modula $\omega_0^2(t)$, definimos

```math
u_{\mathrm{mat}}(t)
=\frac{|\dot{\mathbf P}|^2
+\omega_0^2(t)|\mathbf P|^2}
{2\varepsilon_0\omega_p^2}.
```

La ecuación material da exactamente

```math
\frac{\partial u_{\mathrm{mat}}}{\partial t}
=\mathbf E\cdot\dot{\mathbf P}
-\frac{\gamma}{\varepsilon_0\omega_p^2}
|\dot{\mathbf P}|^2
+\frac{\partial_t\omega_0^2(t)}
{2\varepsilon_0\omega_p^2}|\mathbf P|^2.
```

Al sumar ambos balances,

```math
\frac{\partial}{\partial t}
(u_{\mathrm{EM}}+u_{\mathrm{mat}})
+\nabla\cdot\mathbf S
=-\mathbf E\cdot\mathbf J_f
-p_{\mathrm{diss}}+p_{\mathrm{pump}},
```

con

```math
p_{\mathrm{diss}}
=\frac{\gamma}{\varepsilon_0\omega_p^2}
|\dot{\mathbf P}|^2\ge0,
```

```math
p_{\mathrm{pump}}
=\frac{\partial_t\omega_0^2(t)}
{2\varepsilon_0\omega_p^2}|\mathbf P|^2.
```

La amplificación paramétrica recibe energía del actuador que modifica la rigidez.
Si solo se reemplaza $\gamma$ por $\gamma(t)$ manteniendo $\omega_p$ constante, la
energía almacenada conserva esta forma y
$p_{\mathrm{diss}}=\gamma(t)|\dot{\mathbf P}|^2/(\varepsilon_0\omega_p^2)$; la EDO fenomenológica no produce un término
$\dot\gamma$. Sin embargo, modular físicamente el baño puede requerir potencia y
ruido adicionales. Variar $\omega_p$, la población u otros parámetros que cambian
la normalización de la energía sí exige una nueva derivación microscópica.

### 11.3 Medio instantáneo como caso especial

Para tensores instantáneos reales y simétricos $\boldsymbol\varepsilon(t)$ y
$\boldsymbol\mu(t)$,

```math
u=\frac12\mathbf E^{\mathsf T}\boldsymbol\varepsilon\mathbf E
+\frac12\mathbf H^{\mathsf T}\boldsymbol\mu\mathbf H,
```

y

```math
\frac{\partial u}{\partial t}+\nabla\cdot\mathbf S
=-\mathbf J_f\cdot\mathbf E
-\frac12\mathbf E^{\mathsf T}\dot{\boldsymbol\varepsilon}\mathbf E
-\frac12\mathbf H^{\mathsf T}\dot{\boldsymbol\mu}\mathbf H.
```

La identidad diferencial es algebraicamente válida bajo estas hipótesis. Para que
$u$ sea además una función de almacenamiento no negativa se necesita

```math
\boldsymbol\varepsilon(t)\succ0,
\qquad
\boldsymbol\mu(t)\succ0.
```

Con el signo positivo definido como potencia del actuador hacia el campo, el término
instantáneo de bombeo es

```math
p_{\mathrm{pump}}^{\mathrm{inst}}
=-\frac12\mathbf E^{\mathsf T}
\dot{\boldsymbol\varepsilon}\mathbf E
-\frac12\mathbf H^{\mathsf T}
\dot{\boldsymbol\mu}\mathbf H.
```

Esta expresión no es la energía exacta de un medio dispersivo general. En ese caso
deben conservarse los estados materiales o emplearse una formulación de acción o
campos auxiliares. Para el caso dispersivo estacionario y sin pérdidas, una
derivación exacta se encuentra en
[Philbin (2011)](https://doi.org/10.1103/PhysRevA.83.013823).

### 11.4 Potencia neta y potencia de pared

Definamos primero la potencia global que el actuador entrega al sistema,

```math
P_{\mathrm{pump}}(t)
=\int_V\mathbb E[p_{\mathrm{pump}}(\mathbf r,t)]\,dV.
```

El promedio firmado

```math
\overline P_{\mathrm{pump}}
=\frac1{T_m}\int_0^{T_m}
P_{\mathrm{pump}}(t)\,dt
```

puede ocultar energía inyectada y recuperada dentro del mismo ciclo. Si

```math
P^+(t)=\max\{P_{\mathrm{pump}}(t),0\},
\qquad
P^-(t)=\max\{-P_{\mathrm{pump}}(t),0\},
```

un costo de pared más realista es

```math
P_{\mathrm{wall}}
=\frac{\overline{P^+}}{\eta_{\mathrm{inj}}}
-\eta_{\mathrm{rec}}\overline{P^-}
+P_{\mathrm{bias}}+P_{\mathrm{control}}.
```

Esta elección corresponde a un actuador global. Un arreglo de actuadores locales
puede requerir integrar la parte positiva antes de sumar el volumen; ambas
operaciones no son equivalentes. Si no hay recuperación,
$\eta_{\mathrm{rec}}=0$. Conviene reportar por separado

```math
P_{\mathrm{draw}}
=\frac{\overline{P^+}}{\eta_{\mathrm{inj}}}
+P_{\mathrm{bias}}+P_{\mathrm{control}},
\qquad
P_{\mathrm{rec}}=\eta_{\mathrm{rec}}\overline{P^-},
```

de modo que $P_{\mathrm{wall}}=P_{\mathrm{draw}}-P_{\mathrm{rec}}$. Como el estado
material depende de la señal y del ruido, estas potencias pueden depender también de
la covarianza de entrada.

### 11.5 Cuatro propiedades distintas

Conviene mantener separadas:

| Propiedad | Pregunta |
|---|---|
| Causalidad | ¿La salida depende del futuro? |
| Estabilidad | ¿Las perturbaciones permanecen acotadas o decaen? |
| Pasividad | ¿El sistema puede entregar energía neta desde los puertos considerados? |
| Reciprocidad | ¿Se conserva la respuesta al intercambiar fuente y observador apropiadamente? |

Un medio bombeado puede ser causal y estable, pero activo visto desde los puertos de
señal. La descripción energética completa contiene al menos

```math
\text{puertos de señal}
+\text{puerto de bombeo}
+\text{baños disipativos}.
```

### 11.6 Ganancia no es información gratuita

Una ganancia de potencia $G>1$ puede mejorar la señal frente a ruido añadido
después del dispositivo, pero también amplifica ruido de entrada y requiere bombeo.
En el régimen cuántico, un amplificador lineal insensible a la fase necesita un modo
auxiliar,

```math
\widehat a_{\mathrm{out}}
=\sqrt G\,\widehat a_{\mathrm{in}}
+\sqrt{G-1}\,\widehat b^{\dagger},
```

para preservar los conmutadores. En gran ganancia, el ruido añadido referido a la
entrada no puede ser menor que medio cuanto
([Caves, 1982](https://doi.org/10.1103/PhysRevD.26.1817)).

## 12. Reciprocidad, reversión temporal y dispersión

### 12.1 Reciprocidad LTI

En un medio LTI lineal con las simetrías constitutivas apropiadas, el teorema de
Lorentz relaciona dos soluciones. Tras elegir modos y normalizarlos por potencia,
la matriz de dispersión satisface

```math
\mathbf S=\mathbf S^{\mathsf T}.
```

Esto no exige ausencia de pérdidas. Una red puede ser recíproca y disipativa.

### 12.2 Matriz de dispersión de Floquet

En un dispositivo modulado, un canal exterior se etiqueta por

```math
\alpha=(p,\ell,n),
```

donde $p$ es el puerto, $\ell$ recoge modo y polarización, y $n$ el armónico. La
relación correcta es

```math
b_\alpha(\omega)
=\sum_\beta S^F_{\alpha\beta}(\omega)a_\beta(\omega),
```

con frecuencias físicas $\omega+n\Omega_m$. Comparar solo los coeficientes en la
frecuencia fundamental puede ocultar potencia convertida a otros armónicos.

### 12.3 Qué demuestra no reciprocidad

Para un protocolo de bombeo fijo, una prueba operacional debe comparar los canales
recíprocos completos, con la misma normalización de potencia:

```math
S^F_{\alpha\beta}
\stackrel{?}{=}
S^F_{\widetilde\beta\widetilde\alpha},
```

donde la tilde invierte dirección y asigna correctamente la frecuencia física,
polarización, orden armónico y, cuando aparezcan, modos de frecuencia negativa. Las
relaciones exactas dependen de las simetrías magnetoeléctricas. Una igualdad que
relacione el sistema con el protocolo temporalmente invertido es, en cambio, una
relación de reversión u Onsager–Casimir, no la definición operacional para el
dispositivo bombeado fijo.

La modulación puramente temporal y espacialmente uniforme convierte frecuencias,
pero no distingue por sí sola $+z$ de $-z$. Una modulación viajera introduce el
sesgo de momento $\mathbf K$ y puede romper esa simetría. Aun así, hay que verificar
la matriz multibanda completa.

### 12.4 Reciprocidad no es reversibilidad temporal

La pérdida rompe la reversibilidad temporal, pero no necesariamente la reciprocidad.
Asimismo, mantener fija una modulación viajera al intercambiar transmisor y receptor
no equivale a invertir todo el experimento. La reversión completa exige invertir
también el protocolo externo o su sesgo. Por tanto,

```math
\text{reciprocidad}
\ne
\text{invariancia bajo }t\mapsto-t
\ne
\text{conservación de energía}.
```

### 12.5 Pruebas numéricas

Para cualquier afirmación de no reciprocidad se deberá:

1. incluir todos los armónicos propagantes;
2. distinguir potencia radiada, evanescencia y absorción;
3. usar ondas de puerto normalizadas por potencia;
4. intercambiar los canales físicos completos;
5. verificar el balance de energía incluyendo el bombeo;
6. como diagnóstico adicional, repetir con el sesgo de modulación invertido para
   comprobar que la asimetría sigue al bombeo.

## 13. Ruido, fluctuación–disipación y ciclostacionariedad

### 13.1 Ruido térmico en equilibrio

La disipación y las fluctuaciones no son parámetros independientes. Fijamos además
la convención de espectro simetrizado bilateral

```math
C_{VV}^{\mathrm{sym}}(\tau)
=\frac12\left\langle
\{\widehat V(t+\tau),\widehat V(t)\}
\right\rangle,
```

```math
S_{VV}^{\mathrm{sym}}(\omega)
=\int_{-\infty}^{\infty}
C_{VV}^{\mathrm{sym}}(\tau)e^{\mathrm i\omega\tau}\,d\tau,
```

de modo que

```math
\frac12\left\langle
\{\widehat V(\omega),\widehat V^\dagger(\omega')\}
\right\rangle
=2\pi\delta(\omega-\omega')S_{VV}^{\mathrm{sym}}(\omega).
```

Para una impedancia pasiva en equilibrio,

```math
S_{VV}^{\mathrm{sym}}(\omega)
=\hbar\omega
\coth\left(\frac{\hbar\omega}{2k_{\mathrm B}T_{\mathrm b}}\right)
\,\mathrm{Re}\,Z(\omega),
```

con la convención espectral indicada al comienzo. En el límite clásico,

```math
\hbar\omega\ll k_{\mathrm B}T_{\mathrm b},
```

se obtiene

```math
S_{VV}^{\mathrm{sym}}(\omega)
\longrightarrow
2k_{\mathrm B}T_{\mathrm b}\,\mathrm{Re}\,Z(\omega).
```

Para un resistor, el espectro unilateral por hertz es

```math
S_{VV}^{(1)}(f)=4k_{\mathrm B}T_{\mathrm b}R.
```

Los factores de $2$ y $2\pi$ cambian entre espectros unilaterales, bilaterales y
frecuencia angular; toda simulación debe declarar su convención. El fundamento es
el teorema de fluctuación–disipación de
[Callen y Welton (1951)](https://doi.org/10.1103/PhysRev.83.34).

### 13.2 Oscilador de Langevin

Para una coordenada mecánica equivalente,

```math
M\ddot q+M\gamma\dot q+M\omega_0^2q
=F_{\mathrm{ext}}+\xi(t),
```

el límite clásico de Markov en equilibrio usa

```math
\mathbb E[\xi(t)\xi(t')]
=2M\gamma k_{\mathrm B}T_{\mathrm b}\delta(t-t').
```

Esta expresión muestra por qué no es consistente añadir $\gamma$ al modelo de
Lorentz y escoger luego un AWGN arbitrario sin relación con la temperatura y el
acoplamiento al baño. Al escribir una SDE multiplicativa o calcular energía
estocástica deberá declararse además si se usa Itô o Stratonovich.

### 13.3 El sistema bombeado no está en equilibrio

La FDT de equilibrio no puede aplicarse "instantáneamente" sustituyendo
$\chi(\omega)$ por $\chi(t,\omega)$. En un sistema impulsado, la covarianza depende
también de

- las ocupaciones de los reservorios;
- el protocolo de encendido;
- las fluctuaciones de amplitud y fase del bombeo;
- la creación paramétrica de pares;
- el acoplamiento entre frecuencias positivas y negativas.

La parte antihermítica de una respuesta de dos frecuencias es

```math
\boldsymbol\chi''(\omega,\omega')
=\frac{1}{2\mathrm i}
\left[
\boldsymbol\chi(\omega,\omega')
-\boldsymbol\chi^\dagger(\omega',\omega)
\right].
```

Fuera del equilibrio, conocer $\boldsymbol\chi''$ no determina por sí solo el
espectro simetrizado completo. La teoría debe especificar el estado de los baños.
Un tratamiento de QED macroscópica para medios temporales y sus corrientes de ruido
se desarrolla en
[Horsley y Baker (2025)](https://doi.org/10.1103/PhysRevA.111.053511).

### 13.4 Ruido ciclostacionario

En el régimen periódico de largo plazo, sea

```math
\boldsymbol\mu_n(t)=\mathbb E[\mathbf n(t)],
\qquad
\boldsymbol\mu_n(t+T_m)=\boldsymbol\mu_n(t),
```

y definamos el ruido centrado

```math
\widetilde{\mathbf n}(t)
=\mathbf n(t)-\boldsymbol\mu_n(t).
```

Su covarianza es

```math
\mathbf R_n(t,\vartheta)
=\mathbb E\left[
\widetilde{\mathbf n}\left(t+\frac{\vartheta}{2}\right)
\widetilde{\mathbf n}^\dagger\left(t-\frac{\vartheta}{2}\right)
\right].
```

Para ruido complejo impropio también se necesita la pseudocovarianza

```math
\mathbf C_n(t,\vartheta)
=\mathbb E\left[
\widetilde{\mathbf n}\left(t+\frac{\vartheta}{2}\right)
\widetilde{\mathbf n}^{\mathsf T}
\left(t-\frac{\vartheta}{2}\right)
\right].
```

La ciclostacionariedad de segundo orden exige

```math
\mathbf R_n(t+T_m,\vartheta)=\mathbf R_n(t,\vartheta).
```

Entonces

```math
\mathbf R_n(t,\vartheta)
=\sum_{q\in\mathbb Z}
\mathbf R_n^{(q)}(\vartheta)e^{-\mathrm i q\Omega_m t},
```

y los espectros cíclicos son

```math
\mathbf S_n^{(q)}(\omega)
=\int_{-\infty}^{\infty}
\mathbf R_n^{(q)}(\vartheta)
e^{\mathrm i\omega\vartheta}\,d\vartheta.
```

En frecuencia aparecen correlaciones entre bandas separadas por múltiplos de la
modulación:

```math
\mathbb E[\mathbf N(\omega_1)\mathbf N^\dagger(\omega_2)]
=2\pi\sum_q
\delta(\omega_1-\omega_2-q\Omega_m)
\mathbf S_n^{(q)}
\left(\frac{\omega_1+\omega_2}{2}\right).
```

Un proceso estacionario solo tiene $q=0$. Ignorar $q\ne0$ equivale a declarar
independientes bandas laterales que físicamente pueden estar correlacionadas.
En la base levantada,

```math
[\mathsf S_{N,F}(\omega)]_{mn}
=\mathbf S_n^{(m-n)}
\left(\omega+\frac{m+n}{2}\Omega_m\right).
```

### 13.5 Covarianza periódica del estado

Para

```math
d\mathbf z=\mathbf A(t)\mathbf z\,dt
+\mathbf G(t)d\mathbf w,
```

la covarianza satisface la ecuación de Lyapunov periódica

```math
\dot{\boldsymbol\Sigma}
=\mathbf A\boldsymbol\Sigma
+\boldsymbol\Sigma\mathbf A^\dagger
+\mathbf G\mathbf Q_w\mathbf G^\dagger,
```

con

```math
\boldsymbol\Sigma(t+T_m)=\boldsymbol\Sigma(t).
```

Después de un periodo,

```math
\boldsymbol\Sigma_0
=\mathbf M\boldsymbol\Sigma_0\mathbf M^\dagger
+\mathbf Q_T.
```

Aquí, si $\boldsymbol\Phi$ es el propagador homogéneo dentro del periodo,

```math
\mathbf Q_T
=\int_0^{T_m}
\boldsymbol\Phi(T_m,\tau)
\mathbf G(\tau)\mathbf Q_w(\tau)\mathbf G^\dagger(\tau)
\boldsymbol\Phi^\dagger(T_m,\tau)\,d\tau.
```

Vectorizando,

```math
\mathrm{vec}\,\boldsymbol\Sigma_0
=\left[
\mathbf I-\mathbf M^*\otimes\mathbf M
\right]^{-1}
\,\mathrm{vec}\,\mathbf Q_T.
```

La estabilidad estricta

```math
\rho(\mathbf M)<1.
```

garantiza una solución periódica única, positiva y atractora para todo ruido
admisible. Bajo excitación de todos los modos relevantes también es necesaria; en
casos degenerados como $\mathbf Q_T=\mathbf0$ puede existir una solución algebraica
nula aun para una monodromía inestable.

Esto explica por qué el benchmark inestable actual no puede usarse directamente
para definir una capacidad estacionaria de horizonte infinito.

### 13.6 Ruido observado

El receptor combina distintas fuentes,

```math
\mathbf N_{\mathrm{out}}
=\mathbf H_b\mathbf F_b
+\mathbf H_p\mathbf F_p
+\mathbf N_{\mathrm{rx}},
```

donde $\mathbf F_b$ representa baños materiales, $\mathbf F_p$ fluctuaciones del
bombeo y $\mathbf N_{\mathrm{rx}}$ ruido electrónico posterior. En consecuencia,

```math
\mathbf S_N
=\mathbf H_b\mathbf S_b\mathbf H_b^\dagger
+\mathbf H_p\mathbf S_p\mathbf H_p^\dagger
+\mathbf S_{\mathrm{rx}}
+\text{términos cruzados}.
```

La ubicación de cada fuente es esencial: colocar todo el ruido al final no es
equivalente a introducirlo antes de una etapa paramétrica.

## 14. Del problema de Maxwell al canal de comunicaciones

### 14.1 Definir entradas y salidas físicas

Maxwell relaciona densidades de corriente y campos, pero un canal requiere puertos.
Podemos describir una corriente transmisora mediante funciones base
$\mathbf j_q(\mathbf r)$,

```math
\mathbf J_T(\mathbf r,t)
=\sum_{q=1}^{N_T}x_q(t)\mathbf j_q(\mathbf r),
```

y observables receptores mediante funciones $\mathbf w_p(\mathbf r)$,

```math
y_p(t)=\int_{V_R}
\mathbf w_p^*(\mathbf r)\cdot\mathbf E(\mathbf r,t)\,d^3\mathbf r.
```

Al insertar la Green retardada,

```math
y_p(t)=\sum_q\int_{-\infty}^{t}
H_{pq}(t,t')x_q(t')\,dt'+n_p(t),
```

donde

```math
H_{pq}(t,t')
=\int_{V_R}\!d^3\mathbf r
\int_{V_T}\!d^3\mathbf r'\,
\mathbf w_p^*(\mathbf r)\cdot
\boldsymbol{\mathcal G}_{EJ}
(\mathbf r,\mathbf r';t,t')
\mathbf j_q(\mathbf r').
```

La elección de bases define el canal finito, pero la física procede del operador de
Maxwell.

### 14.2 Ondas de puerto y potencia

En guías, líneas o antenas acopladas se prefieren ondas incidentes y salientes
$a_p$, $b_p$ normalizadas para que

```math
P_p=|a_p|^2-|b_p|^2
```

represente potencia neta en un puerto propagante. En un sistema de Floquet, cada
armónico debe usar la impedancia y velocidad de grupo de su frecuencia física. Una
normalización de amplitud uniforme puede violar el balance de potencia.

### 14.3 Canal armónico levantado

Tomemos la primera zona de Floquet

```math
\mathcal B_F=
\left[-\frac{\Omega_m}{2},\frac{\Omega_m}{2}\right).
```

Para $\omega\in\mathcal B_F$, definimos

```math
\mathbf X_F(\omega)
=\begin{pmatrix}
\vdots\\
\mathbf X(\omega-\Omega_m)\\
\mathbf X(\omega)\\
\mathbf X(\omega+\Omega_m)\\
\vdots
\end{pmatrix}.
```

El canal es

```math
\mathbf Y_F(\omega)
=\mathsf H_F(\omega)\mathbf X_F(\omega)
+\mathbf N_F(\omega).
```

La matriz $\mathsf H_F$ incluye puertos espaciales, polarizaciones y armónicos. La
covarianza $\mathsf S_N(\omega)$ suele tener bloques fuera de la diagonal por la
ciclostacionariedad. Definiremos las densidades espectrales mediante

```math
\mathbb E[\mathbf X_F(\omega)\mathbf X_F^\dagger(\omega')]
=2\pi\delta(\omega-\omega')\mathbf Q(\omega),
```

```math
\mathbb E[\mathbf N_F(\omega)\mathbf N_F^\dagger(\omega')]
=2\pi\delta(\omega-\omega')\mathsf S_N(\omega).
```

### 14.4 Simetría de campos reales

Para señales reales,

```math
\mathbf X(-\omega)=\mathbf X(\omega)^*.
```

Las frecuencias positivas y negativas no son grados de libertad complejos
independientes. Se debe trabajar con señales analíticas, integrar solo media banda o
imponer explícitamente la simetría. De lo contrario, la capacidad puede quedar
duplicada.

### 14.5 Levantamiento periódico en tiempo discreto

Si hay $L$ muestras por periodo, agrupamos

```math
\widetilde{\mathbf x}[k]
=\begin{pmatrix}
\mathbf x[kL]\\
\mathbf x[kL+1]\\
\vdots\\
\mathbf x[kL+L-1]
\end{pmatrix}.
```

Un canal escalar periódico se convierte en un canal MIMO estacionario por bloques,

```math
\widetilde{\mathbf y}[k]
=\sum_r\widetilde{\mathbf H}[r]
\widetilde{\mathbf x}[k-r]
+\widetilde{\mathbf n}[k].
```

Esta técnica conecta la teoría de canales gaussianos periódicos con el análisis
armónico. Requiere que los periodos de canal, ruido y muestreo sean conmensurables;
el muestreo asíncrono puede producir casi-ciclostacionariedad. Si la capacidad del
canal levantado es $C_{\mathrm{bloque}}$, entonces

```math
C_{\mathrm{muestra}}=\frac{C_{\mathrm{bloque}}}{L},
\qquad
C_{\mathrm{s}}=\frac{f_s}{L}C_{\mathrm{bloque}},
```

en bits por muestra original y bits por segundo, respectivamente.

### 14.6 Equivalencia que debemos demostrar

El núcleo temporal y la matriz armónica deberían representar el mismo operador:

```math
\boxed{
\mathcal H(t,t')
\quad\Longleftrightarrow\quad
\mathsf H_F(\omega)
}.
```

Para convertir esta equivalencia formal en un resultado útil necesitamos demostrar:

1. causalidad y periodicidad conjunta;
2. una cota estable, por ejemplo

   ```math
   \|\mathcal H(t,t')\|
   \le Ce^{-\alpha(t-t')}H(t-t'),
   \qquad \alpha>0;
   ```

3. existencia y acotación del operador armónico en el espacio de señales elegido;
4. convergencia de las truncaciones;
5. preservación del balance energético y de la covarianza de ruido.

## 15. Información y capacidad

### 15.1 Entropía e información mutua

Para variables aleatorias continuas,

```math
I(\mathbf X;\mathbf Y)
=h(\mathbf Y)-h(\mathbf Y\mid\mathbf X).
```

Si $\mathbf Z\sim\mathcal{CN}(\mathbf 0,\mathbf K)$ es compleja gaussiana propia
o circular de dimensión $n$, es decir,

```math
\mathbb E[\mathbf Z\mathbf Z^{\mathsf T}]=\mathbf0,
```

entonces

```math
h(\mathbf Z)
=\log\left[(\pi e)^n\det\mathbf K\right]
```

en nats. El logaritmo base $2$ produce bits. La teoría de capacidad comienza con
[Shannon (1948)](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x), pero el modelo
físico de canal y sus restricciones deben definirse antes de aplicar sus resultados.
Un sistema paramétrico sensible a fase puede producir variables impropias. En ese
caso se usa la covarianza aumentada

```math
\widetilde{\mathbf K}_Z
=\begin{pmatrix}
\mathbf K_Z&\mathbf C_Z\\
\mathbf C_Z^*&\mathbf K_Z^*
\end{pmatrix},
\qquad
\mathbf C_Z=\mathbb E[\mathbf Z\mathbf Z^{\mathsf T}],
```

o se trabaja directamente con cuadraturas reales.
En la representación aumentada, una forma típica es

```math
I(\mathbf X;\mathbf Y)
=\frac12\log_2
\frac{\det\widetilde{\mathbf K}_Y}
{\det\widetilde{\mathbf K}_N}.
```

### 15.2 Canal gaussiano MIMO

Para

```math
\mathbf Y=\mathbf H\mathbf X+\mathbf N,
```

con

```math
\mathbf X\sim\mathcal{CN}(\mathbf0,\mathbf Q),
\qquad
\mathbf N\sim\mathcal{CN}(\mathbf0,\mathbf K_N),
```

donde entrada y ruido son independientes, propios y
$\mathbf K_N\succ0$, la información mutua es

```math
I(\mathbf X;\mathbf Y)
=\log_2\det\left[
\mathbf I
+\mathbf K_N^{-1/2}
\mathbf H\mathbf Q\mathbf H^\dagger
\mathbf K_N^{-1/2}
\right].
```

Para vectores reales aparece un factor $1/2$. La capacidad bajo una restricción
ponderada es

```math
C=\max_{\mathbf Q\succeq0}
\log_2\det\left[
\mathbf I
+\mathbf K_N^{-1/2}
\mathbf H\mathbf Q\mathbf H^\dagger
\mathbf K_N^{-1/2}
\right]
```

sujeta a

```math
\mathrm{tr}\,(\mathbf W\mathbf Q)\le P,
\qquad
\mathbf W\succ0.
```

La formulación MIMO clásica está desarrollada en
[Telatar (1999)](https://doi.org/10.1002/ett.4460100604).

### 15.3 Blanqueo y modos informacionales

Definamos el canal blanqueado y ponderado

```math
\mathbf G
=\mathbf K_N^{-1/2}\mathbf H\mathbf W^{-1/2}.
```

Su descomposición singular es

```math
\mathbf G=\mathbf U\boldsymbol\Sigma\mathbf V^\dagger,
\qquad
\boldsymbol\Sigma=\mathrm{diag}(\sigma_1,\ldots,\sigma_r).
```

Con canal y ruido fijos y una única restricción de traza, la potencia óptima se
distribuye mediante *water-filling*,

```math
q_j=\left(\mu-\frac{1}{\sigma_j^2}\right)_+,
```

si $\mathbf K_N\succ0$ y $\mathbf W\succ0$ sobre el subespacio utilizable. El
parámetro $\mu$ se elige para satisfacer la restricción. Los vectores singulares son
modos de comunicación después de tener en cuenta ruido y costo.

### 15.4 Capacidad armónica formal

Para una envolvente compleja y un canal periódico estable, una expresión de tasa es

```math
C
=\frac{1}{2\pi}
\int_{\mathcal B_F}
\log_2\det\left[
\mathbf I
+\mathsf S_N(\omega)^{-1/2}
\mathsf H_F(\omega)
\mathbf Q(\omega)
\mathsf H_F(\omega)^\dagger
\mathsf S_N(\omega)^{-1/2}
\right]d\omega,
```

maximizada sobre $\mathbf Q(\omega)\succeq0$ con

```math
\frac{1}{2\pi}
\int_{\mathcal B_F}
\mathrm{tr}\,
[\mathbf W(\omega)\mathbf Q(\omega)]\,d\omega
\le P_{\mathrm{sig}}.
```

El resultado se expresa en bits por segundo bajo esta normalización. Para campos
reales debe integrarse un conjunto independiente de frecuencias o ajustar el factor.
La matriz completa $\mathbf Q(\omega)$ permite señalización ciclostacionaria
sincronizada con el bombeo; si se exige una entrada estacionaria deben anularse los
bloques cruzados correspondientes y, en general,

```math
C_{\mathrm{stat}}\le C_{\mathrm{cyclo}}.
```

En dimensión infinita, el determinante es de Fredholm. El operador

```math
\mathsf A(\omega)
=\mathsf S_N^{-1/2}\mathsf H_F\mathbf Q
\mathsf H_F^\dagger\mathsf S_N^{-1/2}
```

debe ser positivo y de clase traza, y la inversa del ruido necesita una cota o
condición de integrabilidad que evite direcciones artificialmente sin ruido.

### 15.5 Hipótesis de conocimiento del canal

La capacidad cambia según quién conoce

- la fase $\phi$ del bombeo;
- el estado del canal;
- la forma de onda de modulación;
- las realizaciones del ruido;
- la deriva de sincronización.

Nuestro primer modelo supondrá modulación determinista, fase sincronizada y canal
conocido por transmisor y receptor. Después deberán estudiarse incertidumbre y costo
de estimación. Un error de fase aleatorio puede convertir un canal periódico
coherente en una mezcla estocástica y reducir la ventaja de combinar bandas.

### 15.6 Restricción conjunta de señal y bombeo

Una formulación físicamente completa es

```math
\begin{aligned}
\max_{\boldsymbol\theta,\,\mathbf Q(\omega)}\quad
&C(\boldsymbol\theta,\mathbf Q)\\
\text{sujeto a}\quad
&P_{\mathrm{sig}}(\mathbf Q)
+P_{\mathrm{cost}}(\boldsymbol\theta,\mathbf Q)
\le P_{\mathrm{tot}},\\
&\rho[\mathbf M(\boldsymbol\theta)]\le1-\delta,\\
&\mathbf Q(\omega)\succeq0,\\
&\text{límites de amplitud, velocidad y ancho de banda del actuador}.
\end{aligned}
```

En el primer estudio conservador tomaremos
$P_{\mathrm{cost}}=P_{\mathrm{draw}}$. Una métrica neta con
$P_{\mathrm{cost}}=P_{\mathrm{wall}}$ solo se usará si el mecanismo de recuperación
y su frontera energética están especificados.

El parámetro $\boldsymbol\theta$ contiene profundidad, frecuencia, fase y forma de
la modulación. Para $\boldsymbol\theta$ fijo, la optimización en $\mathbf Q$ es
convexa si canal y ruido no dependen de $\mathbf Q$, el costo de pared es convexo y
no hay saturación ni agotamiento del bombeo. La optimización exterior normalmente no
lo es, porque cambian a la vez canal, ruido, bombeo y estabilidad.

### 15.7 Horizonte finito e inestabilidad

Si $\rho(\mathbf M)\ge1$, no existe en general un régimen ciclostacionario de
horizonte infinito. Todavía puede definirse un canal de bloque finito,

```math
\mathbf y_{N_h}=\mathbf H_{N_h}\mathbf x_{N_h}+\mathbf n_{N_h},
```

con

```math
C_{N_h}^{\mathrm{hor}}
=\frac{1}{T_{\mathrm{obs}}}
\max_{\mathbf K_X\succeq0}
\log_2\det\left[
\mathbf I
+\mathbf K_{N_h}^{-1/2}
\mathbf H_{N_h}\mathbf K_X\mathbf H_{N_h}^\dagger
\mathbf K_{N_h}^{-1/2}
\right],
```

donde $T_{\mathrm{obs}}=N_h\Delta t$ y la tasa queda en bits por segundo. Para
vectores reales aparece el factor $1/2$. Una restricción posible es

```math
\mathrm{tr}\,(\mathbf W_{N_h}\mathbf K_X)
\le E_{N_h}.
```

No puede afirmarse que
$\lim_{N_h\to\infty}C_{N_h}^{\mathrm{hor}}$ existe sin demostrarlo. Esta notación
distingue horizonte $N_h$ de truncamiento Floquet $N_F$. Saturación, no linealidad
y tiempo de apagado también pasan a ser esenciales.

### 15.8 Régimen clásico y cuántico

En radiofrecuencia a temperatura ambiente suele dominar

```math
k_{\mathrm B}T_{\mathrm b}\gg\hbar\omega,
```

y el canal gaussiano clásico es apropiado. En óptica o sistemas criogénicos puede
ocurrir

```math
k_{\mathrm B}T_{\mathrm b}\lesssim\hbar\omega.
```

Entonces deben emplearse cuadraturas, canales bosónicos gaussianos y restricciones
de número de fotones; la fórmula clásica de log-determinante no basta cuando la
modulación mezcla operadores de creación y aniquilación.

## 16. Límites físicos del canal

### 16.1 Modos espaciales entre volúmenes

A frecuencia fija, el operador de Green entre corrientes transmisoras y campos
receptores puede escribirse como

```math
\mathcal G:\mathcal J_T\longrightarrow\mathcal E_R.
```

Su descomposición singular

```math
\mathcal G\mathbf v_j=\sigma_j\mathbf u_j
```

define pares óptimos de modos transmisor–receptor. Si $\mathcal G$ es
Hilbert–Schmidt,

```math
\sum_j\sigma_j^2=\|\mathcal G\|_{\mathrm{HS}}^2.
```

La apertura, la separación, el volumen y la longitud de onda limitan cuántos
$\sigma_j$ son útiles. La compacidad sola solo garantiza $\sigma_j\to0$, no la suma
cuadrática. También deben fijarse normas físicas, regiones disjuntas o una
regularización de la singularidad de Green. La formulación de
[Miller (2000)](https://doi.org/10.1364/AO.39.001681) establece esta idea para ondas
escalares; el caso electromagnético vectorial requiere el operador y productos
internos correspondientes.

### 16.2 Operador espacio–Floquet

La modulación amplía el espacio a

```math
\mathcal G_F:
\mathcal J_T\otimes\ell^2(\mathbb Z)
\longrightarrow
\mathcal E_R\otimes\ell^2(\mathbb Z).
```

El índice armónico crea puertos de frecuencia, pero no garantiza infinitos grados
de libertad utilizables. La apertura, el ancho de banda, la regularidad de la
modulación y la geometría controlan el decaimiento del operador físico. Potencia y
ruido no cambian sus valores singulares brutos, pero determinan cuáles son útiles a
través del operador informacional

```math
\mathcal G_{\mathrm{info}}
=\mathsf S_N^{-1/2}\mathcal G_F\mathbf W^{-1/2}.
```

### 16.3 Bode–Fano

Las cotas clásicas de adaptación toman una forma cualitativa como

```math
\int_0^\infty
w(\omega)\ln\frac{1}{|\Gamma(\omega)|}\,d\omega
\le B_{\mathrm{carga}}.
```

El resultado original trata una carga dada y una red de adaptación reactiva, pasiva
e invariante en el tiempo. Añadir pérdida puede reducir reflexión absorbiendo energía
sin mejorar la transferencia útil. Una red conmutada puede superar esa cota
particular porque abandona una hipótesis, no porque viole causalidad. El resultado de
conmutación citado corresponde a pulsos finitos y no demuestra por sí solo una
mejora de capacidad periódica de horizonte infinito. La comparación justa debe
incluir energía de conmutación, ruido y radiación fuera de banda; véanse
[Fano (1950)](https://doi.org/10.1016/0016-0032%2850%2990006-8) y
[Shlivinski y Hadad (2018)](https://doi.org/10.1103/PhysRevLett.121.204301).

### 16.4 Límites materiales

En ciertas cotas de respuesta absorbente para sistemas pasivos, locales y LTI
aparecen figuras como

```math
\frac{|\chi(\omega)|^2}{\mathrm{Im}\,\chi(\omega)}.
```

En un medio temporal, $\chi$ es un operador de dos frecuencias. Sustituir
directamente la figura escalar no es válido, y cuando
$`\mathrm{Im}\,\chi\to0`$ pueden dominar límites radiativos o de unitariedad. Una
posible contribución matemática es derivar cotas en términos de la parte
antihermítica del operador $\boldsymbol\chi(\omega,\omega')$ y del trabajo de
bombeo.

### 16.5 Velocidad de señal

Velocidad de fase, velocidad de grupo, velocidad de energía y velocidad de frente
no son equivalentes. Dispersión anómala o ganancia pueden producir velocidades de
grupo mayores que $c$ sin transmisión superlumínica de información. La causalidad
completa se expresa en el soporte espacio-temporal de la Green retardada, no solo en
el valor de $d\omega/dk$. La pasividad lineal general también impone cotas a la
velocidad de energía
([Welters, Avniel y Johnson, 2014](https://doi.org/10.1103/PhysRevA.90.023847)).

## 17. Estado del arte hasta agosto de 2026

### 17.1 Línea histórica mínima

| Año | Resultado consolidado | Consecuencia para nosotros |
|---:|---|---|
| 1950 | Zadeh formuló el análisis bifrecuencial de redes variables. | El núcleo LTV y la transferencia de dos frecuencias tienen antecedentes clásicos. |
| 1958 | Morgenthaler estudió modulación temporal de la velocidad electromagnética. | Conversión de frecuencia y energía en medios temporales no son fenómenos nuevos. |
| 1963–1967 | Cassedy y Oliner derivaron interacciones estables e inestables en medios periódicos espacio–tiempo. | Las bandas y la amplificación paramétrica espacio-temporal ya poseen teoría temprana. |
| 1971 | Fante trató transmisión hacia medios variables, incluso dispersivos. | Las interfaces temporales dispersivas tienen antecedentes de más de medio siglo. |
| 2009 | Zurita-Sánchez, Halevi y Cervantes-González resolvieron el *scattering* de una losa periódica en el tiempo. | Una matriz multibanda para una región finita tampoco es por sí sola novedad. |
| 2014 | Xiao, Maywar y Agrawal precisaron reflexión y transmisión en una frontera temporal ideal. | Las condiciones temporales deben derivarse y normalizarse con cuidado. |
| 2017–2020 | Se desarrollaron y demostraron dispositivos con modulación viajera, aislamiento y cristales de velocidad uniforme. | La no reciprocidad requiere un sesgo espacio-temporal y comparación multibanda. |
| 2021 | Solís, Kastner y Engheta resolvieron una discontinuidad temporal en un medio Lorentz dispersivo. | La dispersión y los estados materiales son indispensables. |
| 2023 | Se observó reflexión temporal y traducción de frecuencia de banda ancha. | Las fronteras temporales ya cuentan con evidencia experimental directa. |
| 2024 | Sloan et al. derivaron respuesta lineal microscópica y propiedades ópticas de materiales dispersivos dependientes del tiempo. | La respuesta de dos tiempos y su energía tienen una base microscópica moderna. |
| 2025 | Sun, Fan y Hu formularon Maxwell dispersivo y disipativo como problema matricial de Floquet. | "Floquet dispersivo" ya no es un reclamo de novedad defendible. |
| 2025 | Horsley y Baker desarrollaron QED macroscópica y corrientes de ruido para medios temporales. | El ruido no estacionario empieza a derivarse desde la física, no solo a prescribirse. |
| 2025 | Galiffi et al. mostraron que las condiciones de una interfaz temporal dependen de su implementación microscópica. | El actuador debe formar parte del modelo. |
| 2026 | Guo et al. demostraron un cristal temporal plasmónico totalmente óptico en terahercios, con modulación subciclo. | La frontera experimental ya incluye modulación fuerte y dispersiva. |
| 2026 | Sustaeta-Osuna et al. propusieron electrodinámica fluctuacional exacta de dos frecuencias para medios dispersivos temporales. | Es una referencia muy reciente y provisional para conectar respuesta, pérdidas y fluctuaciones. |

Fuentes primarias representativas:
[Zadeh (1950)](https://doi.org/10.1109/JRPROC.1950.231083),
[Morgenthaler (1958)](https://doi.org/10.1109/TMTT.1958.1124533),
[Cassedy y Oliner (1963)](https://doi.org/10.1109/PROC.1963.2566),
[Fante (1971)](https://doi.org/10.1109/TAP.1971.1139931),
[Zurita-Sánchez et al. (2009)](https://doi.org/10.1103/PhysRevA.79.053821),
[Solís et al. (2021)](https://doi.org/10.1364/PRJ.427368),
[Moussa et al. (2023)](https://doi.org/10.1038/s41567-023-01975-y),
[Sloan et al. (2024)](https://doi.org/10.1021/acsphotonics.3c00773),
[Sun, Fan y Hu (2025)](https://doi.org/10.1103/lcmw-qrrp),
[Horsley y Baker (2025)](https://doi.org/10.1103/PhysRevA.111.053511),
[Guo et al. (2026)](https://doi.org/10.1038/s41586-026-10825-9) y el preprint de
[Sustaeta-Osuna et al. (2026)](https://arxiv.org/abs/2607.22340).

### 17.2 Qué está bien establecido

La literatura ya contiene, por separado:

- relaciones constitutivas causales de dos tiempos;
- modelos Lorentz y Drude modulados;
- interfaces temporales y conversión de frecuencia;
- Floquet, monodromía, bandas laterales y cristales fotónicos temporales;
- *scattering* de regiones espacio-temporales finitas;
- amplificación paramétrica y puntos excepcionales;
- dispositivos no recíprocos con modulación viajera;
- teoría de canales gaussianos MIMO y periódicos;
- ruido térmico de equilibrio y primeros tratamientos de ruido temporal fuera del
  equilibrio;
- modos electromagnéticos de comunicación entre aperturas o volúmenes.

### 17.3 Qué sigue poco unificado

No encontramos una teoría estándar única que comience en un medio Maxwell–Lorentz
con actuador y baños, y termine en una capacidad de canal incluyendo simultáneamente

```math
\text{causalidad de dos tiempos},
```

```math
\text{estabilidad y error de truncamiento de Floquet},
```

```math
\text{normalización de puertos y balance del bombeo},
```

```math
\text{ruido ciclostacionario derivado de la disipación},
```

```math
\text{restricción conjunta de señal, bombeo y geometría}.
```

Esta conclusión es una evaluación del panorama, no una prueba definitiva de
novedad. Antes de publicar habrá que realizar una revisión sistemática por cada
teorema o cota concreta.

### 17.4 Qué no debemos reclamar como nuevo

No sería defendible presentar como contribución original únicamente:

```math
\text{"un oscilador de Lorentz modulado"},
```

```math
\text{"aplicar Floquet a un medio dispersivo"},
```

```math
\text{"obtener bandas laterales"},
```

```math
\text{“observar resonancia cerca de }\Omega_m=2\omega_0\text{”},
```

o una aplicación directa del log-determinante a una matriz armónica prescrita.

### 17.5 Lectura correcta de los cristales temporales

En este contexto, "cristal fotónico temporal" significa una propiedad óptica
impuesta periódicamente,

```math
\varepsilon(t+T_m)=\varepsilon(t),
```

no el cristal temporal cuántico de muchos cuerpos que rompe espontáneamente una
simetría temporal. Conviene evitar esa ambigüedad en títulos y resúmenes.

## 18. Dirección de investigación propuesta

### 18.1 Enunciado de trabajo

El programa más coherente es

```math
\boxed{
\text{Maxwell--Lorentz causal}
\longrightarrow
\text{Floquet estable}
\longrightarrow
\text{Green y transferencia armónica}
\longrightarrow
\text{ruido físico}
\longrightarrow
\text{capacidad con costo de bombeo}
}.
```

Un título técnico provisional sería:

> **Capacidad de canales electromagnéticos causales de Floquet con dispersión,
> ruido físico y restricción conjunta de señal y bombeo.**

### 18.2 Primer posible teorema

Para un sistema Maxwell–Lorentz periódico, causal y exponencialmente estable,
buscar hipótesis bajo las cuales:

1. la Green retardada satisface

   ```math
   \mathcal G_R(t,s)=0\quad\text{para }t<s,
   ```

   ```math
   \mathcal G_R(t+T_m,s+T_m)=\mathcal G_R(t,s);
   ```

2. existe una cota

   ```math
   \|\mathcal G_R(t,s)\|
   \le Ce^{-\alpha(t-s)}H(t-s);
   ```

3. su transformación armónica define un operador acotado

   ```math
   \mathsf H_F(\omega):
   \ell^2\longrightarrow\ell^2;
   ```

4. las proyecciones armónicas $\mathsf P_{N_F}$ satisfacen primero convergencia fuerte
   sobre entradas de energía finita,

   ```math
   \mathsf P_{N_F}\mathsf H_F\mathsf P_{N_F}\mathbf x
   \longrightarrow\mathsf H_F\mathbf x;
   ```

5. bajo hipótesis adicionales de compacidad, Hilbert–Schmidt o decaimiento uniforme,
   se obtiene una cota en norma y la tasa de capacidad truncada converge,

   ```math
   C_{N_F}^{\mathrm{Floquet}}\longrightarrow C.
   ```

La tasa de convergencia debería relacionarse con la suavidad de la modulación, la
distancia al umbral paramétrico y la separación de resonancias.

### 18.3 Segundo posible resultado

Definir y resolver

```math
C^*(P_{\mathrm{tot}})
=\sup_{\boldsymbol\theta,\mathbf Q}
C(\boldsymbol\theta,\mathbf Q)
```

sujeto a

```math
P_{\mathrm{sig}}(\mathbf Q)
+P_{\mathrm{cost}}(\boldsymbol\theta,\mathbf Q)
\le P_{\mathrm{tot}},
```

```math
\rho[\mathbf M(\boldsymbol\theta)]\le1-\delta.
```

Una pregunta falsable es si la eficiencia

```math
\eta_C^{\mathrm{gross}}
=\frac{C}
{P_{\mathrm{sig}}+P_{\mathrm{draw}}}
```

permanece acotada cuando $\rho(\mathbf M)\to1^-$. La ganancia crece cerca del
umbral, pero también pueden crecer ruido, sensibilidad y costo de bombeo.

### 18.4 Tercer posible resultado

Buscar una desigualdad de ruido–ganancia de dos frecuencias,

```math
\mathsf S_N
\succeq
\mathcal F
(\mathsf H_F,\boldsymbol\chi'',T_m,T_{\mathrm b},\text{baños}),
```

que generalice el vínculo entre disipación, ganancia y ruido a un sistema
electromagnético temporal. Esta línea es más profunda y probablemente exigirá
formalismo cuántico o de sistemas abiertos.

### 18.5 Hipótesis iniciales conservadoras

Para que el primer resultado sea abordable, comenzaremos con:

- geometría unidimensional o una línea de transmisión;
- material eléctrico local con una sola resonancia de Lorentz;
- modulación sinusoidal de $\omega_0^2(t)$;
- parámetros reales y bombeo determinista;
- régimen estrictamente estable;
- puertos lineales normalizados por potencia;
- ruido clásico gaussiano de baños térmicos en una primera aproximación;
- número finito de bandas, seguido de un estudio explícito de convergencia.

La anisotropía, bianisotropía, no localidad, saturación y cuantización se añadirán
solo después de validar esta cadena.

## 19. Relación con el modelo ya implementado

### 19.1 Ecuación actual

El proyecto usa

```math
\ddot P+\gamma\dot P
+\omega_0^2
[1+m\cos(\Omega_m t+\phi)]P
=\varepsilon_0\omega_p^2E.
```

Con

```math
\tau=\omega_0t,
\qquad
\zeta=\frac{\gamma}{2\omega_0},
\qquad
\nu=\frac{\Omega_m}{\omega_0},
```

obtenemos

```math
p''+2\zeta p'
+[1+m\cos(\nu\tau+\phi)]p=f.
```

El núcleo causal es

```math
g(\tau,s)
=\mathbf e_p^{\mathsf T}
\mathbf U(\tau,s)\mathbf bH(\tau-s).
```

### 19.2 Qué hemos demostrado computacionalmente

El repositorio ya verifica:

1. causalidad del núcleo para $\tau<s$;
2. composición del propagador;
3. periodicidad conjunta

   ```math
   g(\tau+T_\tau,s+T_\tau)=g(\tau,s);
   ```

4. límite LTI cuando $m=0$;
5. identidad de Liouville

   ```math
   \det\mathbf M=e^{-2\zeta T_\tau};
   ```

6. balance de energía adimensional;
7. detección de la lengua principal de Mathieu.

### 19.3 Dos benchmarks

Para

```math
\zeta=0.02,
\qquad
m=0.20,
\qquad
\nu=2,
```

se obtiene

```math
\rho(\mathbf M)\approx1.09865>1,
```

por lo que el caso es inestable y sirve como prueba de detección de resonancia, no
como canal estacionario.

Con

```math
\nu=3,
```

se obtiene

```math
\rho(\mathbf M)\approx0.95898<1,
\qquad
g_{\max}\approx-0.02,
```

y este será el benchmark para el canal de horizonte largo.

### 19.4 Qué todavía no demuestra el código

El modelo actual no contiene aún:

- propagación espacial ni condiciones de frontera;
- puertos electromagnéticos normalizados;
- matriz armónica y prueba de convergencia;
- ruido derivado de los baños materiales;
- costo de pared del modulador;
- capacidad de Shannon;
- incertidumbre del bombeo;
- mecanismo microscópico completo del actuador.

### 19.5 Siguiente resultado reproducible

El siguiente hito debe comparar, en el benchmark estable, dos cálculos del mismo
mapa entrada–salida:

```math
\text{integral con }g(\tau,s)
\quad\text{frente a}\quad
\text{matriz armónica }\mathsf H_F^{(N_F)}.
```

Para entradas multisinusoidales y pulsos, el error relativo

```math
\epsilon_{N_F}
=\frac{\|y_{\mathrm{tiempo}}-y_{\mathrm{Floquet}}^{(N_F)}\|_2}
{\|y_{\mathrm{tiempo}}\|_2}
```

debe tender a cero al aumentar $N_F$. Este resultado crea el puente necesario antes
de introducir ruido y capacidad.

## 20. Jerarquía de validación científica

Cada nivel depende de los anteriores:

### Nivel 1: unidades y convenciones

- todas las ecuaciones deben ser dimensionalmente homogéneas;
- la convención de Fourier debe permanecer fija;
- $f$ y $\omega$ deben relacionarse por $\omega=2\pi f$;
- amplitud, energía y potencia deben distinguirse.

### Nivel 2: límites analíticos

- $m\to0$ recupera Lorentz LTI;
- $\gamma\to0$ recupera el límite sin pérdidas;
- $\Omega_m\to0$ concuerda con una variación cuasiestática cuando esta aproximación
  sea válida;
- la solución numérica coincide con la exponencial matricial para coeficientes
  constantes.

### Nivel 3: causalidad y estabilidad

- soporte retardado exacto;
- composición del propagador;
- Liouville;
- espectro de Floquet independiente de la fase inicial;
- margen $1-\rho(\mathbf M)$ documentado.

### Nivel 4: energía

- residuo de Poynting decrece al refinar malla y paso temporal;
- pérdida, señal y bombeo se registran por separado;
- la suma coincide con el cambio de energía almacenada y el flujo de frontera.

### Nivel 5: equivalencia de representaciones

- respuesta temporal y armónica coinciden;
- resultados convergen con el número de bandas;
- se conserva la simetría de realidad;
- los armónicos de borde llevan energía despreciable.

### Nivel 6: ruido

- la covarianza es hermítica y semidefinida positiva;
- el límite LTI recupera Nyquist o la FDT elegida;
- la covarianza periódica satisface Lyapunov;
- las correlaciones cruzadas de bandas no se eliminan artificialmente.

### Nivel 7: información

- capacidad invariante bajo cambios unitarios de base;
- blanqueo del ruido verificado;
- optimización de covarianza satisface KKT;
- la capacidad converge con tiempo, muestreo y truncamiento;
- el costo incluye señal y bombeo.

### Nivel 8: comparación experimental

- parámetros vinculados a un mecanismo realizable;
- amplitud y velocidad de modulación dentro de límites de actuador;
- pérdidas, dispersión y ruido medidos;
- incertidumbres y barras de error propagadas al resultado final.

## 21. Método de trabajo matemático y computacional

### 21.1 Herramienta principal

Python es suficiente y, para este proyecto, la opción principal recomendada. El
ecosistema mínimo es:

- NumPy y SciPy para álgebra lineal, integración y optimización;
- SymPy para comprobaciones simbólicas, no como sustituto de una demostración;
- Matplotlib para diagramas de estabilidad y convergencia;
- Jupyter para exploración reproducible;
- pytest para identidades analíticas y regresión numérica;
- CVXPY para optimización convexa de covarianzas cuando lleguemos a capacidad.

MATLAB puede ser útil si después necesitamos toolboxes institucionales, Simulink o
comparar con un laboratorio que ya lo use, pero no es necesario instalarlo para la
teoría ni para los próximos hitos.

### 21.2 Papel del cálculo a mano

Cada resultado debe pasar por tres representaciones:

```math
\text{derivación en LaTeX}
\longrightarrow
\text{implementación numérica}
\longrightarrow
\text{prueba automática}.
```

El cálculo manual fija hipótesis, signos y unidades. El cálculo numérico explora
regímenes donde no hay forma cerrada. Las pruebas impiden que una refactorización
rompa identidades físicas.

### 21.3 Escalamiento

Antes de integrar conviene adimensionalizar. Si $t_c$, $E_c$ y $P_c$ son escalas,

```math
\tau=\frac{t}{t_c},
\qquad
e=\frac{E}{E_c},
\qquad
p=\frac{P}{P_c}.
```

Los grupos adimensionales revelan la física y mejoran el condicionamiento. No se
debe confundir adimensionalización con elegir unidades arbitrarias: las escalas
deben conservarse para reconstruir energía y potencia SI.

### 21.4 Precisión y condicionamiento

Cerca de una resonancia o punto excepcional, el problema puede ser no normal y mal
condicionado. Deben registrarse

```math
\kappa(\mathbf V)=\|\mathbf V\|\|\mathbf V^{-1}\|,
```

para la matriz de autovectores, el residuo

```math
r_j=\frac{\|\mathbf M\mathbf v_j-\lambda_j\mathbf v_j\|}
{\|\mathbf M\|\|\mathbf v_j\|},
```

y, cuando sea necesario, el seudoespectro. Un autovalor con muchas cifras impresas
no es necesariamente preciso si el problema está mal condicionado.

### 21.5 Reproducibilidad

Cada figura o tabla científica deberá poder regenerarse con:

1. un archivo de parámetros;
2. una semilla si hay aleatoriedad;
3. una versión registrada del código;
4. tolerancias y método numérico explícitos;
5. datos fuente guardados además de la imagen;
6. una prueba o referencia analítica.

## 22. Diagnóstico y ruta de nivelación

### 22.1 Cómo autoevaluarte

Asigna a cada bloque una puntuación:

```math
0=\text{no puedo empezarlo},
\qquad
1=\text{lo resuelvo con apuntes},
\qquad
2=\text{lo resuelvo y explico sin apuntes}.
```

No hace falta obtener $2$ en todo antes de investigar. Sí conviene alcanzar $2$ en
los bloques A–E y al menos $1$ en F–I antes de formular teoremas de capacidad.

#### Bloque A: cálculo vectorial y Maxwell

Debes poder derivar

```math
\nabla\cdot(\mathbf E\times\mathbf H)
=\mathbf H\cdot(\nabla\times\mathbf E)
-\mathbf E\cdot(\nabla\times\mathbf H)
```

y, a partir de ella, el teorema de Poynting. También debes explicar de dónde salen
las cuatro condiciones de frontera espaciales.

**Si obtienes 0:** repasa gradiente, divergencia, rotacional, teoremas de Gauss y
Stokes.

**Si obtienes 1:** deriva Poynting sin memorizarlo y resuelve una onda plana en un
dieléctrico.

**Criterio de dominio:** puedes comprobar unidades y signos de cada término.

#### Bloque B: Fourier, Laplace y distribuciones

Debes calcular

```math
\mathcal F\{H(t)e^{-at}\}
=\frac{1}{a-\mathrm i\omega},
\qquad a>0,
```

con nuestra convención, ubicar su polo y explicar por qué es causal. Debes manejar
$\delta(t)$, convolución, Parseval y la diferencia entre hertz y radianes por
segundo.

**Si obtienes 0:** estudia transformadas desde señales LTI.

**Si obtienes 1:** trabaja contornos simples y distribuciones.

**Criterio de dominio:** puedes cambiar de tiempo a frecuencia sin perder factores
$2\pi$.

#### Bloque C: variable compleja y causalidad

Debes explicar por qué

```math
\chi(z)=\int_0^\infty\chi(t)e^{\mathrm izt}\,dt
```

es analítica para $`\mathrm{Im}\,z>0`$ y obtener una relación de
Kramers–Kronig mediante Cauchy.

**Si obtienes 0:** repasa funciones analíticas, residuos y valor principal.

**Si obtienes 1:** estudia Hilbert, Titchmarsh y relaciones sustraídas.

**Criterio de dominio:** puedes diagnosticar una susceptibilidad con un polo en el
semiplano incorrecto.

#### Bloque D: sistemas lineales y estado

Debes resolver

```math
\dot{\mathbf x}=\mathbf A\mathbf x+\mathbf B\mathbf u
```

con exponencial matricial y demostrar

```math
\mathbf U(t,s)=\mathbf U(t,u)\mathbf U(u,s).
```

También debes conocer autovalores, SVD, adjuntos, matrices positivas y ecuaciones de
Lyapunov.

**Si obtienes 0:** repasa álgebra lineal y EDO.

**Si obtienes 1:** estudia no normalidad, controlabilidad y observabilidad.

**Criterio de dominio:** puedes construir una función de Green desde una realización
de estado.

#### Bloque E: Floquet y perturbación

Debes calcular numéricamente una monodromía, verificar Liouville y explicar por qué

```math
\mu_j=\frac1{T_m}\,\mathrm{Log}\,\lambda_j
```

tiene ramas. Debes reproducir el umbral aproximado $m>4\zeta$.

**Si obtienes 0:** estudia ecuaciones periódicas, matriz fundamental y Mathieu.

**Si obtienes 1:** estudia promediado, múltiples escalas y perturbación de
autovalores.

**Criterio de dominio:** distingues estabilidad modal, transitoria y forzada.

#### Bloque F: métodos numéricos

Debes poder explicar error local y global, rigidez, tolerancias adaptativas y
convergencia de malla. Como prueba, verifica experimentalmente

```math
|\det\mathbf M-e^{-2\zeta T_\tau}|\to0
```

al reducir tolerancias.

**Si obtienes 0:** repasa Runge–Kutta y álgebra numérica.

**Si obtienes 1:** estudia integradores preservadores de estructura y
seudoespectros.

**Criterio de dominio:** no confundes convergencia aparente con exactitud física.

#### Bloque G: procesos aleatorios

Debes manejar media, autocovarianza y densidad espectral. Demuestra que una
covarianza válida satisface

```math
\mathbf K=\mathbf K^\dagger\succeq0.
```

Después resuelve una ecuación de Lyapunov estacionaria y una periódica.

**Si obtienes 0:** estudia variables gaussianas y procesos estacionarios.

**Si obtienes 1:** añade procesos ciclostacionarios, SDE y espectros cruzados.

**Criterio de dominio:** puedes construir ruido correlacionado sin producir una
covarianza no positiva.

#### Bloque H: información y optimización

Debes derivar la capacidad escalar

```math
C=B\log_2(1+\mathrm{SNR})
```

bajo sus hipótesis, y luego obtener la forma MIMO log-determinante. Debes conocer
Lagrangianos, condiciones KKT y convexidad en $\mathbf Q$.

**Si obtienes 0:** estudia entropía, información mutua y canal AWGN.

**Si obtienes 1:** añade canales coloreados, MIMO y *water-filling*.

**Criterio de dominio:** puedes identificar exactamente qué cambia cuando el ruido
es correlacionado.

#### Bloque I: física de materiales y ruido

Debes derivar $\chi_L(\omega)$ desde la EDO, separar energía almacenada y disipada,
y explicar el límite de Drude. Después debes relacionar pérdida y ruido mediante
FDT, declarando convención espectral.

**Si obtienes 0:** estudia Lorentz, Drude y polaritones.

**Si obtienes 1:** añade respuesta lineal de Kubo, baños y QED macroscópica.

**Criterio de dominio:** nunca agregas ganancia, pérdida o ruido sin identificar su
reservorio energético.

### 22.2 Plan de dieciséis semanas

#### Semanas 1–2: fundamentos matemáticos

- Fourier y Laplace con nuestra convención;
- distribuciones y funciones de Green;
- variable compleja y Kramers–Kronig;
- entrega: derivación completa del Lorentz LTI y prueba numérica de KK.

#### Semanas 3–4: Maxwell y energía

- Maxwell macroscópico y condiciones de frontera;
- Poynting en vacío, medio instantáneo y Lorentz;
- entrega: cuaderno que cierre el balance energético dimensional y adimensional.

#### Semanas 5–6: sistemas LTV causales

- propagadores, Duhamel y núcleos de dos tiempos;
- periodicidad conjunta y análisis bifrecuencial;
- entrega: reconstruir una salida con la integral causal para varias entradas.

#### Semanas 7–8: Floquet

- monodromía, exponentes, Mathieu y no normalidad;
- balance armónico y convergencia de truncamiento;
- entrega: equivalencia numérica tiempo–Floquet en el benchmark estable.

#### Semanas 9–10: propagación espacial

- línea de transmisión o losa Maxwell–Lorentz unidimensional;
- puertos, potencia, fronteras y *scattering* multibanda;
- entrega: matriz $S^F$ con balance de energía y prueba de reciprocidad.

#### Semanas 11–12: ruido

- Langevin, FDT y Lyapunov periódico;
- ruido ciclostacionario y covarianza armónica;
- entrega: espectro de ruido que recupere Nyquist cuando $m\to0$.

#### Semanas 13–14: información

- canal gaussiano coloreado, MIMO y *water-filling*;
- capacidad de bloque y tasa armónica;
- entrega: capacidad del benchmark estable con modulación fija.

#### Semanas 15–16: problema conjunto

- potencia de señal, bombeo neto y costo de pared;
- margen de estabilidad y optimización externa;
- entrega: primera frontera de Pareto

  ```math
  (C,P_{\mathrm{draw}},P_{\mathrm{rec}},1-\rho(\mathbf M)).
  ```

### 22.3 Referencias de estudio por nivel

Para comenzar conviene combinar textos de base con artículos primarios:

- Maxwell y ondas: un texto avanzado de electromagnetismo de ingeniería;
- sistemas: estado, Lyapunov y Floquet;
- señales: Fourier, LTV y procesos aleatorios;
- información: Shannon, canales gaussianos y MIMO;
- materiales: Lorentz–Drude, respuesta lineal y fluctuación–disipación;
- frontera actual: los artículos anotados en la sección 25.

La lectura de artículos no sustituye los ejercicios. El criterio real de nivel es
poder reproducir una derivación y detectar cuándo fallan sus hipótesis.

## 23. Errores frecuentes que deben evitarse

1. Usar $\mathbf D(t)=\varepsilon(t)\mathbf E(t)$ cerca de una resonancia sin
   estados materiales.
2. Confundir dispersión temporal con variación temporal.
3. Aplicar Kramers–Kronig LTI a una "permitividad congelada".
4. Confundir causalidad, estabilidad, pasividad y reciprocidad.
5. Usar $|\det\mathbf M|<1$ como prueba de estabilidad.
6. Ignorar crecimiento transitorio de un operador no normal.
7. Aplicar una fórmula estacionaria cuando $\rho(\mathbf M)\ge1$.
8. Atribuir amplificación al medio sin contabilizar el bombeo.
9. Modular $\omega_0$, $\omega_0^2$, $\omega_p^2$ o $\gamma$ como si fueran el
   mismo mecanismo.
10. Imponer condiciones temporales sin modelar posibles fuentes impulsivas.
11. Comparar solo $S_{21}$ y $S_{12}$ en la frecuencia fundamental.
12. Llamar no recíproca a cualquier conversión asimétrica.
13. Añadir amortiguamiento sin un modelo de fluctuaciones.
14. Aplicar FDT de equilibrio a un medio bombeado sin justificación.
15. Diagonalizar artificialmente el ruido entre bandas laterales.
16. Contar frecuencias positivas y negativas dos veces.
17. Truncar Floquet sin medir convergencia y energía en los bordes.
18. Invertir una covarianza casi singular y aceptar una capacidad enorme sin
   regularización física.
19. Comparar con Bode–Fano sin decir qué hipótesis se abandonó.
20. Optimizar capacidad solo con potencia de señal y declarar gratuita la
   modulación.
21. Confundir potencia neta recuperable con potencia consumida desde la pared.
22. Presentar una reproducción de Mathieu como resultado nuevo.
23. Usar una malla más fina como única validación, sin límite analítico.
24. Omitir unidades, convención de Fourier o normalización modal.
25. Convertir una oportunidad plausible de investigación en una afirmación de
   novedad antes de una búsqueda sistemática.

## 24. Glosario esencial

**Analiticidad:** diferenciabilidad compleja; conecta causalidad temporal con
restricciones espectrales.

**Banda lateral:** componente en $\omega+n\Omega_m$ producida por un sistema
periódico.

**Bianisotropía:** acoplamiento constitutivo eléctrico–magnético cruzado.

**Causalidad:** ausencia de respuesta anterior a la excitación.

**Ciclostacionariedad:** periodicidad de las estadísticas de un proceso aleatorio.

**Cuasifrecuencia:** frecuencia de Floquet definida módulo $\Omega_m$.

**Dispersión espacial:** respuesta no local en posición o dependencia con
$\mathbf k$.

**Dispersión temporal:** memoria material o dependencia con $\omega$.

**Estabilidad exponencial:** decaimiento acotado por $Ce^{-\alpha(t-s)}$.

**FDT:** teorema de fluctuación–disipación que relaciona pérdida y ruido en
equilibrio.

**Función de Green retardada:** respuesta a una fuente impulsiva que se anula antes
de la fuente.

**Herglotz:** función analítica con parte imaginaria positiva en el semiplano
superior; aparece en sistemas pasivos.

**LPTV:** sistema lineal periódicamente variable en el tiempo.

**Matriz monodrómica:** propagador a lo largo de un periodo.

**Multiplicador de Floquet:** autovalor de la monodromía.

**No normalidad:** condición
$\mathbf A\mathbf A^\dagger\ne\mathbf A^\dagger\mathbf A$; permite gran
crecimiento transitorio.

**Pasividad:** incapacidad de entregar energía neta sin una reserva inicial desde
los puertos incluidos.

**Punto excepcional:** degeneración no hermítica donde coalescen autovalores y
autovectores.

**Reciprocidad:** simetría apropiada al intercambiar fuente y observador.

**Respuesta de dos tiempos:** núcleo que depende separadamente del instante de
observación y del de excitación.

**Ruido coloreado:** ruido con covarianza no proporcional a la identidad o espectro
no plano.

**Transferencia armónica:** matriz infinita que relaciona bandas laterales de
entrada y salida.

**Water-filling:** asignación óptima de potencia entre modos gaussianos paralelos.

## 25. Bibliografía primaria anotada

### 25.1 Fundamentos

1. [Maxwell, “A Dynamical Theory of the Electromagnetic Field”
   (1865)](https://doi.org/10.1098/rstl.1865.0008). Fundamento de la teoría de campo
   y de la corriente de desplazamiento.
2. [Poynting, “On the Transfer of Energy in the Electromagnetic Field”
   (1884)](https://doi.org/10.1098/rstl.1884.0016). Ley local de transporte de
   energía.
3. [Drude, “Zur Elektronentheorie der Metalle”
   (1900)](https://doi.org/10.1002/andp.19003060312). Modelo clásico de portadores
   libres.
4. [Toll, “Causality and the Dispersion Relation: Logical Foundations”
   (1956)](https://doi.org/10.1103/PhysRev.104.1760). Relación rigurosa entre
   causalidad, analiticidad y dispersión.
5. [Kubo, “Statistical-Mechanical Theory of Irreversible Processes I”
   (1957)](https://doi.org/10.1143/JPSJ.12.570). Respuesta lineal microscópica.

### 25.2 Sistemas variables y medios espacio-temporales

6. [Zadeh, “Frequency Analysis of Variable Networks”
   (1950)](https://doi.org/10.1109/JRPROC.1950.231083). Análisis bifrecuencial de
   sistemas LTV.
7. [Morgenthaler, “Velocity Modulation of Electromagnetic Waves”
   (1958)](https://doi.org/10.1109/TMTT.1958.1124533). Antecedente directo de los
   medios temporales.
8. [Cassedy y Oliner, “Dispersion Relations in Time-Space Periodic Media: Part I”
   (1963)](https://doi.org/10.1109/PROC.1963.2566). Interacciones estables.
9. [Cassedy, “Dispersion Relations in Time-Space Periodic Media: Part II”
   (1967)](https://doi.org/10.1109/PROC.1967.5775). Interacciones inestables.
10. [Fante, “Transmission of Electromagnetic Waves into Time-Varying Media”
    (1971)](https://doi.org/10.1109/TAP.1971.1139931). Conmutación y dispersión.
11. [Zurita-Sánchez, Halevi y Cervantes-González, *scattering* de una losa temporal
    (2009)](https://doi.org/10.1103/PhysRevA.79.053821). Región finita periódica.
12. [Xiao, Maywar y Agrawal, frontera temporal
    (2014)](https://doi.org/10.1364/OL.39.000574). Reflexión y transmisión
    temporales.
13. [Taravati et al., *scattering* no recíproco de una losa espacio-temporal
    (2017)](https://doi.org/10.1103/PhysRevB.96.165144). Conversión direccional.
14. [Li et al., método de matriz de transferencia espacio-temporal
    (2019)](https://doi.org/10.1103/PhysRevB.100.144311). Herramienta general de
    análisis.
15. [Moussa et al., observación de reflexión temporal
    (2023)](https://doi.org/10.1038/s41567-023-01975-y). Evidencia experimental.

### 25.3 Dispersión, causalidad y energía

16. [Tip, “Linear Absorptive Dielectrics”
    (1998)](https://doi.org/10.1103/PhysRevA.57.4818). Campos auxiliares para medios
    absorbentes.
17. [Philbin, “Electromagnetic Energy Momentum in Dispersive Media”
    (2011)](https://doi.org/10.1103/PhysRevA.83.013823). Energía exacta desde un
    principio de acción.
18. [Welters, Avniel y Johnson, límites en medios pasivos
    (2014)](https://doi.org/10.1103/PhysRevA.90.023847). Herglotz, energía y
    causalidad.
19. [Solís y Engheta, respuesta de polarización LTV
    (2021)](https://doi.org/10.1103/PhysRevB.103.144303). Causalidad de dos tiempos.
20. [Solís, Kastner y Engheta, discontinuidad Lorentz
    (2021)](https://doi.org/10.1364/PRJ.427368). Dispersión en una interfaz temporal.
21. [Sloan et al., propiedades ópticas dispersivas dependientes del tiempo
    (2024)](https://doi.org/10.1021/acsphotonics.3c00773). Respuesta microscópica y
    Kramers–Kronig generalizadas.
22. [Sun, Fan y Hu, Maxwell dispersivo como matriz de Floquet
    (2025)](https://doi.org/10.1103/lcmw-qrrp). Formulación moderna del problema de
    autovalores.
23. [Galiffi et al., electrodinámica de interfaces temporales
    (2025)](https://doi.org/10.1038/s41377-025-01947-2). Papel del mecanismo
    microscópico.
24. [Guo et al., cristal temporal plasmónico
    (2026)](https://doi.org/10.1038/s41586-026-10825-9). Realización totalmente
    óptica en terahercios.

### 25.4 Ruido e información

25. [Nyquist, “Thermal Agitation of Electric Charge in Conductors”
    (1928)](https://doi.org/10.1103/PhysRev.32.110). Ruido térmico de una impedancia.
26. [Callen y Welton, “Irreversibility and Generalized Noise”
    (1951)](https://doi.org/10.1103/PhysRev.83.34). FDT general.
27. [Gardner, teoría espectral de ciclostacionariedad
    (1986)](https://doi.org/10.1016/0165-1684%2886%2990092-7). Correlaciones
    cíclicas.
28. [Horsley y Baker, QED y corrientes de ruido temporales
    (2025)](https://doi.org/10.1103/PhysRevA.111.053511). Ruido fuera del equilibrio.
29. [Sustaeta-Osuna et al., electrodinámica fluctuacional temporal
    (preprint, 2026)](https://arxiv.org/abs/2607.22340). Marco de dos frecuencias;
    debe citarse explícitamente como preprint.
30. [Shannon, “A Mathematical Theory of Communication”
    (1948)](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x). Fundamento de
    entropía y capacidad.
31. [Telatar, capacidad de canales gaussianos multiantena
    (1999)](https://doi.org/10.1002/ett.4460100604). Log-determinante MIMO.
32. [Miller, modos de comunicación entre volúmenes
    (2000)](https://doi.org/10.1364/AO.39.001681). Grados de libertad físicos.
33. [Caves, límites cuánticos de amplificación
    (1982)](https://doi.org/10.1103/PhysRevD.26.1817). Ruido mínimo añadido.
34. [Shlezinger y Dabora, capacidad de canales periódicos
    (2015)](https://doi.org/10.1109/TCOMM.2015.2408318). Levantamiento de canales y
    ruido periódicos.

## 26. Criterio de preparación para el siguiente hito

Estamos listos para avanzar de teoría a implementación cuando podamos demostrar y
reproducir, sin saltos conceptuales,

```math
\boxed{
\begin{aligned}
&\text{causalidad del núcleo},\\
&\text{estabilidad estricta de Floquet},\\
&\text{balance de energía con bombeo},\\
&\text{equivalencia tiempo--armónicos},\\
&\text{convergencia al aumentar }N_F.
\end{aligned}
}
```

Solo entonces introduciremos el primer baño térmico y la capacidad gaussiana. Este
orden no retrasa la teoría de información: evita optimizar un canal que todavía no
es físicamente consistente.
