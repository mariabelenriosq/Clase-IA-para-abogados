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
- [ ] **M4 — Interfaz web desplegada** *(Sesión 4)*: tu herramienta tiene **URL pública** (ver Parte 4) y tu primer usuario real la probó con evidencia.
- [ ] **M5 — Análisis crítico y demo** *(Sesión 5)*: Parte 7 completada + presentación de 5 minutos.
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
[Usuario] → [Interfaz web] → [Orquestación (LangChain)] → [Modelo (OpenRouter)] ↕ [Tu corpus normativo (RAG)]



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
- [ ] URL pública funciona en el navegador de otra persona (pídele a alguien que la abra)
- [ ] La advertencia de la Parte 7 es **visible** en la interfaz
- [ ] No hay API keys ni secretos en el código (verifica con una búsqueda de `sk-` en el repo)
- [ ] Anota la URL aquí: **`[tu-url-publica]`**
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
  - [ ] Implementada y visible en la interfaz
- **Protección de datos (Ley 1581 de 2012).** Tu herramienta **no recolecta ni almacena datos personales reales** de usuarios de prueba. Los usuarios de prueba usan situaciones ficticias o datos inventados.
  - [ ] Verificado: no guardo datos personales
- **Corpus público.** Solo fuentes públicas: leyes, decretos, jurisprudencia publicada.
  - [ ] Verificado
- **Anti-alucinaciones.** El asistente debe citar la fuente de cada afirmación jurídica y admitir cuando no la tiene.
  - [ ] Casos de prueba donde la herramienta se niega a inventar
---
## 🔍 Parte 7 — Análisis crítico (insumo de tu sustentación final)
Responde con total honestidad — aquí es donde demuestras tu criterio jurídico:
1. **¿Dónde falla tu herramienta?** Describe 2 situaciones donde se equivoca o se queda corta.
2. **¿Qué datos procesa?** Qué entra, qué se guarda, qué sale.
3. **¿Por qué no reemplaza al abogado?** Argumenta en 5–8 frases.
---
## ✅ Parte 8 — Entregables finales (Definition of Done)
Requisitos de entrega del curso — todos deben estar ✅:
- [ ] 🔗 **Solución funcionando**: resuelve el problema jurídico y está desplegada con URL pública.
- [ ] 👤 **Usuario real**: al menos una persona externa al curso la usó, con evidencia (video corto o testimonio). Guarda la evidencia en `docs/evidencia-usuario.md`.
- [ ] 📦 **Repositorio con historial**: este repo muestra tus avances semanales (commits + bitácora).
- [ ] 🧠 **Análisis crítico**: Parte 7 completada.
- [ ] 📋 Partes 1–7 de este README completas y al día.
---
*Construido con asistencia de IA — como se enseña en este curso.* 🧑‍⚖️🤖
