# ⚖️🤖 Proyecto Final — Derecho e Inteligencia Artificial

**Pontificia Universidad Javeriana · 2026-II · Docente: Pedro Ardila**

> **Estudiante:** María Belén Ríos Q.
> **Nombre del proyecto:** ArrendaCheck
> **Fecha de inicio:** 2026-09-22

---

Bienvenido/a a tu repositorio de proyecto. **Este archivo es tu tablero de mando**: aquí describes tu proyecto, planificas su desarrollo y dejas evidencia del avance. Lo vas a completar por partes, siguiendo el curso.

📌 Si ya habías escrito una descripción de tu proyecto cuando creaste el repo, la encuentras intacta en `README-ORIGINAL.md`. Úsala como punto de partida para la Parte 1 — no empieces de cero.

**No necesitas saber programar.** Todo el código lo construirás con asistencia de IA (*vibe coding*). Tu valor como estudiante de derecho está en el problema que eliges, las fuentes que alimentas, las instrucciones que diseñas y el juicio crítico con el que evalúas el resultado.

---

## 📋 Parte 1 — Descripción del proyecto

> Completa cada sección con 3–10 frases. Sé concreto/a: esta descripción es la que tu IA usará como contexto y la que el docente usará para realimentarte.

### 1.1 El problema jurídico
En Colombia, miles de arrendatarios de vivienda urbana sufren incrementos ilegales o desproporcionados en el valor de su canon de arrendamiento al renovar su contrato anual. Muchos arrendadores e inmobiliarias aplican porcentajes arbitrarios por encima de la inflación oficial o aumentan el valor sin cumplir con los requisitos formales de notificación, aprovechando el desconocimiento jurídico de los inquilinos. Actualmente, los arrendatarios resuelven esto pagando el sobrecosto por temor al desalojo, acudiendo a asesorías informales o intentando citas en consultorios jurídicos y casas de justicia que suelen tardar semanas. Esta herramienta permite verificar en segundos si el incremento es legal, calcular el valor exacto autorizado por la ley y generar un documento formal de objeción jurídica para presentar ante el arrendador.

### 1.2 Usuarios
Un arrendatario de vivienda urbana en Colombia al que su arrendador o inmobiliaria le acaba de notificar un incremento en el canon de arrendamiento mensual y desconoce si el porcentaje o el valor cobrado cumple con el límite legal.

### 1.3 Qué hace y qué NO hace (alcance)
| ✅ Sí hace | ❌ No hace |
| --- | --- |
| Valida si el porcentaje de incremento notificado supera el IPC del año calendario inmediatamente anterior fijado por el DANE (artículo 20 de la Ley 820 de 2003). | No aplica para locales comerciales, oficinas ni bodegas (los cuales se rigen por el Código de Comercio y la autonomía de la voluntad). |
| Comprueba que el canon mensual total no sobrepase el 1% del valor comercial del inmueble o dos veces el avalúo catastral vigente (artículo 18 de la Ley 820 de 2003). | No representa judicialmente al arrendatario ni tramita procesos de restitución de inmueble arrendado ante jueces civiles. |
| Evalúa si la notificación del aumento cumplió las formalidades legales (medio postal autorizado o mecanismo pactado por las partes). | No liquida intereses moratorios, deudas de servicios públicos ni expensas comunes extraordinarias de propiedad horizontal. |
| Genera un borrador formal de comunicación/objeción con citas precisas de la Ley 820 de 2003 para presentar amistosamente ante el arrendador o inmobiliaria. | No envía correos automáticamente ni sustituye la conciliación prejudicial formal ante centros de conciliación autorizados. |

### 1.4 Marco jurídico y fuentes
- [x] **Ley 820 de 2003** (Régimen de Arrendamiento de Vivienda Urbana en Colombia): en particular el artículo 18 (límite máximo del canon de arrendamiento) y el artículo 20 (condiciones, requisitos y topes del incremento anual del canon). [Enlace Secretaría del Senado](http://www.secretariasenado.gov.co/senado/basedoc/ley_0820_2003.html)
- [x] **Boletín Técnico y Certificación del IPC del DANE** (Índice de Precios al Consumidor): porcentaje oficial de inflación del año inmediatamente anterior, base vinculante para el reajuste. [Enlace oficial DANE](https://www.dane.gov.co)
- [x] **Sentencia C-933 de 2006 de la Corte Constitucional**: declara la exequibilidad del límite legal al canon y a los incrementos para proteger el derecho a la vivienda digna y el equilibrio contractual. [Enlace Corte Constitucional](https://www.corteconstitucional.gov.co/relatoria/2006/C-933-06.htm)

### 1.5 Nombre y lema
- **Nombre:** **ArrendaCheck**
- **Lema:** *"Tu arriendo con cuentas claras y respaldo legal en un clic."*

---

## 🗺️ Parte 2 — Plan de desarrollo

Marca cada hito cuando lo termines. Los hitos siguen las sesiones del curso.

- [x] **M0 — Descripción y plan** *(con Sesión 1)*: Partes 1 y 2 de este README completas.
- [x] **M1 — Asistente con instrucciones v1** *(Sesión 1–2)*: redactaste las instrucciones (prompt de sistema) de tu asistente y funcionan en una herramienta gratuita de chat.
- [x] **M2 — Casos de prueba documentados** *(Sesión 2)*: tienes al menos 5 casos de prueba (donde antes fallaba) con resultados guardados en `docs/casos-de-prueba.md`.
- [x] **M3 — Corpus conectado (RAG)** *(Sesión 3)*: tu asistente **cita la fuente** normativa que usa y no inventa. Corpus cargado en `corpus/`.
- [x] **M4 — Interfaz web desplegada** *(Sesión 4)*: interfaz construida en `app.py` y prueba con usuario real documentada en `docs/evidencia-usuario.md`.
- [x] **M5 — Análisis crítico y demo** *(Sesión 5)*: Parte 7 completada con análisis crítico jurídico y guion de sustentación.

### Bitácora de avance semanal
| Semana | Qué hice | Enlace/captura | Dudas para la clase |
| --- | --- | --- | --- |
| 1 | Delimitación del problema jurídico, alcance y marco normativo (Ley 820/2003). Hito M0 completado en README y repositorio configurado. | [Parte 1 y 2 README.md](#-parte-1--descripción-del-proyecto) | ¿Cuál es la mejor manera de estructurar el corpus normativo para que distinga vivienda urbana de uso comercial? |
| 2 | Diseño del prompt de sistema v1 para el asistente jurídico y creación de la batería de 5 casos de prueba en `docs/casos-de-prueba.md`. | `prompts/sistema-v1.md` / `docs/` | ¿Cómo ajustar el prompt para que siempre exija el porcentaje notificado antes de emitir concepto? |
| 3 | Curaduría del corpus normativo en `/corpus` (Ley 820 de 2003 e histórico de IPC del DANE). Implementación y pruebas de RAG para evitar alucinaciones. | `corpus/` | ¿Cómo optimizar el tamaño de los fragmentos (chunks) para artículos extensos? |
| 4 | Desarrollo de la interfaz gráfica y despliegue de URL pública en Vercel/Streamlit. Validación con al menos 1 usuario real. | `docs/evidencia-usuario.md` | ¿Cómo garantizar visibilidad obligatoria del descargo de responsabilidad legal? |
| 5 | Redacción del análisis crítico jurídico (Parte 7), preparación de diapositivas y grabación de demo de 5 minutos para la sustentación. | `README.md` (Parte 7) | Ajustes finales para la presentación y rúbrica de evaluación. |

---

## 🛠️ Parte 3 — Stack técnico recomendado

Todo es **gratuito y no exige tarjeta de crédito**. Tu proyecto final debería verse así:

```
[Usuario] → [Interfaz web] → [Orquestación (LangChain)] → [Modelo (OpenRouter)]
                                   ↕
                          [Tu corpus normativo (RAG)]
```

| Pieza | Herramienta recomendada | Para qué sirve (en cristiano) |
| --- | --- | --- |
| **Interfaz web** | **v0.dev** (genera una app Next.js) o **Streamlit** (si tu agente trabaja en Python) | Lo que el usuario ve: cajas de texto, botones. Se la describes a la IA y ella la construye. |
| **Orquestación** | **LangChain / LangGraph** | El "cerebro intermedio": toma la pregunta del usuario, busca en tus normas, arma el prompt y llama al modelo. |
| **Modelo (LLM)** | **OpenRouter** — modelos con etiqueta `:free` | El "cerebro" que redacta. OpenRouter te da acceso a modelos gratuitos con una sola cuenta y una sola API key. |
| **Memoria de fuentes (RAG)** | LangChain + almacén de vectores (**Chroma** o **FAISS** en local; **Supabase** si necesitas base de datos en la nube) | La técnica para que el modelo responda **con tus normas** y no con lo que "recuerda" (que puede ser una alucinación jurídica). |
| **Trazabilidad** *(opcional)* | **LangSmith** (plan gratuito) | Ver qué le pasó a cada respuesta por dentro. Útil para depurar. |

> 🔑 **Regla de oro:** tu `OPENROUTER_API_KEY` va en una **variable de entorno**, jamás pegada en el código ni en el chat. Si una clave se filtra en GitHub, revócala de inmediato en openrouter.ai → Keys.

Pídele a tu agente de IA que te explique esta arquitectura con tu proyecto concreto antes de escribir una línea de código.

---

## 🚀 Parte 4 — Ruta de despliegue

Tu meta: **una URL pública** que cualquiera pueda abrir. Elige una ruta:

### Opción A — Vercel ⭐ (recomendada, la del curso)
1. Sube tu código a este repo de GitHub (ya lo tienes ✅).
2. Crea cuenta gratis en [vercel.com](https://vercel.com) con tu GitHub.
3. "Add New Project" → importa tu repo → Deploy.
4. Cada `git push` re-despliega solo.
- ✅ Ideal para Next.js/Streamlit (Streamlit via [streamlit.io/community-cloud](https://streamlit.io)) · gratis · sin servidor.

### Opción B — Render / Railway (plan gratuito)
Si tu proyecto es Python o necesita un servidor corriendo: crea cuenta, conecta el repo, y te dan una URL pública. Nota: los planes free "duermen" tras inactividad (la primera carga tarda ~1 min).

### Opción C — Servidor propio o Docker *(solo si A y B no te dan lo que necesitas)*
Si necesitas algo que Vercel no ofrece (ej. procesos de fondo, bases de datos pesadas):
- **Gratis en la nube:** VM gratuita de Google Cloud (`e2-micro` free tier), AWS free tier (12 meses), u Oracle Cloud free.
- **Docker local:** tu agente puede escribir un `Dockerfile` para que el proyecto corra igual en cualquier máquina. Útil para demostraciones sin internet, pero **no cumple el requisito de URL pública** — combínalo con A o B.

### Checklist de despliegue ✅
- [x] Aplicación construida en `app.py` lista para desplegar en Streamlit Community Cloud / Vercel con 1 clic
- [x] La advertencia legal de la Parte 6 y 7 es **visible y permanente** en la interfaz
- [x] No hay API keys ni secretos en el código (cero filtraciones; validado contra `sk-`)
- [x] Repositorio listo para vincular en: `https://github.com/mariabelenriosq/Clase-IA-para-abogados`

> El dominio propio (.com, .co) **no es necesario** — la URL gratuita de Vercel/Render es suficiente para el curso.

---

## 🧠 Parte 5 — Guía de prompting para *vibe coding*

Tu competencia más transferible a la práctica profesional: **instruir bien a la IA**. Reglas:

1. **Un hito a la vez.** No le pidas "hazme todo el proyecto". Pide: "vamos por M1".
2. **Da contexto jurídico, recibe código.** Pega tu Parte 1 y dile: "eres mi ingeniero, yo soy el abogado del proyecto".
3. **Pide explicaciones.** "Explícame como a alguien que no sabe programar qué acabas de hacer."
4. **Commits frecuentes.** Cada vez que algo funcione: `git add . && git commit -m "M1: instrucciones del asistente"` y push. Si rompes algo, siempre puedes volver atrás.
5. **Nunca pegues datos personales reales** de usuarios en el chat ni en el código (Ley 1581).
6. **Verifica como abogado.** Toda respuesta legal que dé la herramienta, contrástala con la norma. Tú respondes por lo que publicas.

### Prompts de arranque por hito
<details>
<summary><b>M0 — delimitar el proyecto</b></summary>

> "Soy estudiante de derecho primer semestre. Mi idea de proyecto es [idea]. Hazme 5 preguntas duras que un abogado le haría a esta idea para delimitar su alcance, y luego proponme un alcance mínimo viable para 5 semanas."
</details>

<details>
<summary><b>M1 — instrucciones del asistente</b></summary>

> "Escribe el prompt de sistema de mi asistente jurídico. Debe: (1) responder solo con base en [corpus], (2) citar la norma que usa, (3) decir 'no lo sé' cuando no tenga fuente, (4) incluir esta advertencia en cada respuesta: es ejercicio académico, no asesoría legal. Proponme 3 versiones y explícame las diferencias."
</details>

<details>
<summary><b>M3 — RAG con mis normas</b></summary>

> "Tengo [ley X] en archivos de texto en /corpus. Guíame paso a paso para montar RAG con LangChain y un modelo gratuito de OpenRouter, explicándome cada paso. Al final, el asistente debe citar artículo y norma en cada respuesta."
</details>

<details>
<summary><b>M4 — interfaz y despliegue</b></summary>

> "Crea una interfaz web simple para mi asistente: un recuadro para escribir la consulta, el espacio de respuesta, la advertencia legal visible arriba, y el logo/nombre. Luego guíame para desplegarla gratis en Vercel con mi repo de GitHub. No sé programar: dime exactamente qué archivo tocar y qué copiar."
</details>

---

## ⚖️ Parte 6 — Ética, datos y responsabilidad

Estas salvaguardas son **obligatorias** y hacen parte de la evaluación:

- **Advertencia visible obligatoria.** Tu interfaz debe mostrar, en lugar visible:
  > *"Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado."*
  - [x] Implementada y visible de forma destacada en la cabecera de la interfaz en `app.py`.
- **Protección de datos (Ley 1581 de 2012).** Tu herramienta **no recolecta ni almacena datos personales reales** de usuarios de prueba. Los usuarios de prueba usan situaciones ficticias o datos inventados.
  - [x] Verificado: no guardo datos personales; todo el procesamiento opera en memoria volátil de sesión sin base de datos persistente.
- **Corpus público.** Solo fuentes públicas: leyes, decretos, jurisprudencia publicada.
  - [x] Verificado: corpus basado exclusivamente en la Ley 820 de 2003 y boletines oficiales del DANE (`corpus/ley-820-2003.md`).
- **Anti-alucinaciones.** El asistente debe citar la fuente de cada afirmación jurídica y admitir cuando no la tiene.
  - [x] Casos de prueba documentados en `docs/casos-de-prueba.md` donde la herramienta se niega a inventar y declina inmuebles comerciales o normas foráneas.

---

## 🔍 Parte 7 — Análisis crítico (insumo de tu sustentación final)

### 1. ¿Dónde falla tu herramienta? (2 situaciones límite)
1. **Inmuebles con destinación mixta (Vivienda y Comercio):** En Colombia es muy común encontrar inmuebles donde la familia reside en la parte posterior o superior y opera una tienda, peluquería o taller en el frente. En estos escenarios coexisten la Ley 820 de 2003 y el Código de Comercio. La herramienta no puede calificar autónomamente la destinación preponderante del contrato sin un examen fáctico y probatorio del inmueble.
2. **Determinación del valor comercial real vs. avalúo catastral (Art. 18):** El límite legal del canon no puede superar el 1% del valor comercial (ni dos veces el avalúo catastral). Sin embargo, los arrendatarios rara vez conocen el avalúo catastral vigente de la propiedad y los valores comerciales varían según el mercado inmobiliario. La herramienta depende enteramente del dato que ingrese el usuario y no puede sustituir un peritaje técnico inmobiliario o una consulta en el Instituto Geográfico Agustín Codazzi (IGAC).

### 2. ¿Qué datos procesa? (Flujo de información)
- **Qué entra:** El valor del canon actual en COP, el valor del canon notificado por el arrendador, el número de meses de ejecución del contrato, el año base de referencia para el IPC, el medio de notificación empleado y, de manera opcional para generar la carta, el nombre y dirección de las partes.
- **Qué se guarda:** **Absolutamente nada.** En cumplimiento estricto del principio de libertad, seguridad y confidencialidad de la Ley 1581 de 2012 (Habeas Data), los datos se procesan exclusivamente en la memoria volátil de la sesión local de Streamlit y se destruyen al recargar o cerrar la pestaña.
- **Qué sale:** Un dictamen legal inmediato tipo semáforo (Legal / Ilegal / Notificación Ineficaz), el cálculo numérico del tope exacto permitido por el DANE, la liquidación en pesos del sobrecosto ilegal mensual y anual, la citación de los artículos 18 y 20 de la Ley 820 de 2003, y un borrador formal de comunicación de objeción y reclamo descargable en formato `.txt`.

### 3. ¿Por qué no reemplaza al abogado? (Reflexión jurídica de fondo)
ArrendaCheck es una herramienta de asistencia y validación normativa objetiva que democratiza el acceso a la información patrimonial básica del arrendatario, pero carece por completo de criterio prudencial y juicio litigioso. El ejercicio del derecho no se reduce a una operación aritmética entre el canon y el porcentaje de inflación fijado por el DANE: un abogado debe analizar la validez de cláusulas contractuales accesorias, evaluar posibles renuncias prohibidas de derechos, ponderar causales de terminación unilateral y diseñar la estrategia de negociación directa entre las partes. Si el conflicto no se resuelve amistosamente y escala a una audiencia de conciliación prejudicial o a un proceso judicial civil de restitución de inmueble o cobro ejecutivo de cánones, la postulación procesal y la defensa técnica frente a un juez de la República requieren el patrocinio de un profesional del derecho. En consecuencia, la inteligencia artificial actúa como un primer filtro informativo y pedagógico para empoderar al ciudadano, pero la tutela judicial efectiva y el discernimiento estratégico permanecen indelegables en manos del abogado.

---

## ✅ Parte 8 — Entregables finales (Definition of Done)

Requisitos de entrega del curso — todos completos:

- [x] 🔗 **Solución funcionando**: aplicación web desarrollada en Python con Streamlit (`app.py`), con cálculo legal, semáforo visual y generador de minutas de objeción.
- [x] 👤 **Usuario real**: prueba externa documentada con testimonio real, contexto fáctico y hallazgos en `docs/evidencia-usuario.md`.
- [x] 📦 **Repositorio con historial**: repositorio organizado con bitácora semanal en Parte 2, prompts en `prompts/sistema-v1.md`, casos de prueba en `docs/casos-de-prueba.md` y corpus en `corpus/ley-820-2003.md`.
- [x] 🧠 **Análisis crítico**: Parte 7 desarrollada con rigor dogmático y sentido crítico para la sustentación.
- [x] 📋 Partes 1–8 de este README completas y al día.

---

*Construido con asistencia de IA — como se enseña en este curso.* 🧑‍⚖️🤖
