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
- [ ] **M1 — Asistente con instrucciones v1** *(Sesión 1–2)*: redactaste las instrucciones (prompt de sistema) de tu asistente y funcionan en una herramienta gratuita de chat.
- [ ] **M2 — Casos de prueba documentados** *(Sesión 2)*: tienes al menos 5 casos de prueba (donde antes fallaba) con resultados guardados en `docs/casos-de-prueba.md`.
- [ ] **M3 — Corpus conectado (RAG)** *(Sesión 3)*: tu asistente **cita la fuente** normativa que usa y no inventa. Corpus cargado en `corpus/`.
- [ ] **M4 — Interfaz web desplegada** *(Sesión 4)*: tu herramienta tiene **URL pública** (ver Parte 4) y tu primer usuario real la probó con evidencia.
- [ ] **M5 — Análisis crítico y demo** *(Sesión 5)*: Parte 7 completada + presentación de 5 minutos.

### Bitácora de avance semanal
| Semana | Qué hice | Enlace/captura | Dudas para la clase |
| --- | --- | --- | --- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

## 🛠️ Parte 3 — Stack técnico recomendado

Todo es **gratuito y no exige tarjeta de crédito**. Tu proyecto final debería verse así:
