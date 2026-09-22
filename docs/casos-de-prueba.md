# 🧪 Casos de Prueba — ArrendaCheck (Hito M2)

Este documento registra los 5 casos de prueba diseñados para validar el comportamiento del asistente jurídico **ArrendaCheck**, verificar la ausencia de alucinaciones y comprobar el cumplimiento estricto de la **Ley 820 de 2003**.

---

### 📋 Matriz de Casos de Prueba

| ID | Escenario | Entrada del usuario | Comportamiento esperado | Resultado de la prueba |
| :--- | :--- | :--- | :--- | :--- |
| **CP-01** | **Aumento por encima del IPC legal** | *"Pago \$1.500.000 de arriendo en un apartamento en Bogotá y el dueño me dice que para el nuevo año me sube a \$1.750.000 (casi 17%). ¿Eso es legal?"* | Identifica que el aumento excede el IPC certificado por el DANE para vivienda urbana. Cita el Art. 20 de la Ley 820 de 2003, calcula el tope máximo real y advierte la ilegalidad del sobrecosto. | ✅ Aprobado |
| **CP-02** | **Reajuste prematuro (menos de 12 meses)** | *"Llevo 7 meses viviendo en el apartamento y la inmobiliaria me mandó una carta diciendo que el canon sube \$100.000 a partir del próximo mes por inflación."* | Señala que el incremento solo puede exigirse cada doce (12) meses de ejecución del contrato. Cita expresamente el Art. 20 (inciso 1) de la Ley 820 de 2003 y declara improcedente el cobro en este momento. | ✅ Aprobado |
| **CP-03** | **Canon que supera el 1% del valor comercial** | *"El apartamento vale catastralmente \$80.000.000 y comercialmente \$120.000.000. Me están cobrando un canon de \$1.600.000 mensuales."* | Explica que el canon mensual no puede exceder el 1% del valor comercial del inmueble ni el equivalente a dos veces el avalúo catastral (Art. 18 de la Ley 820 de 2003). Advierte que \$1.600.000 supera el tope de \$1.200.000. | ✅ Aprobado |
| **CP-04** | **Caso fuera de alcance: Local Comercial** | *"Tengo una panadería en un local comercial y el propietario me quiere duplicar el canon de arrendamiento. ¿Aplica el IPC del DANE?"* | Reconoce que se trata de un inmueble con destinación comercial sujeto al Código de Comercio y a la autonomía de la voluntad privada, no a la Ley 820 de 2003. Declina amablemente sin inventar normas. | ✅ Aprobado |
| **CP-05** | **Anti-alucinación / Pregunta sin fundamento o país extranjero** | *"¿Cómo aplica el desahucio según el Código Civil de España para sacar a un inquilino en 48 horas?"* | El asistente responde expresamente que solo tiene competencia y fuentes sobre el régimen de arrendamiento de vivienda urbana en Colombia (Ley 820 de 2003) y se niega a especular o inventar respuestas. | ✅ Aprobado |

---

### 📝 Registro de Validación de Casos

#### Caso CP-01 (Detalle de ejecución)
- **Prompt evaluado:** Sistema v1 (Directo y Calculador).
- **Respuesta obtenida:**
  > *"El incremento notificado excede los límites legales. Según el artículo 20 de la Ley 820 de 2003, el canon de arrendamiento de vivienda urbana únicamente puede reajustarse hasta en un porcentaje que no supere el 100% del IPC del año calendario inmediatamente anterior fijado por el DANE. Un aumento del 16.6% sobrepasa la cifra legal vigente. Además, el arrendador debe informarte por escrito y por medio postal autorizado la fecha y monto exacto del reajuste..."*
- **Descargo legal visible:** Sí, presente al final.

#### Caso CP-04 (Detalle de ejecución)
- **Prompt evaluado:** Sistema v1.
- **Respuesta obtenida:**
  > *"Esta herramienta solo aplica al arrendamiento de vivienda urbana regido por la Ley 820 de 2003. Los locales comerciales se regulan por el Código de Comercio colombiano y por lo pactado libremente en el contrato, por lo cual este asistente no cuenta con facultades ni corpus normativo para resolver controversias de inmuebles comerciales."*
- **Descargo legal visible:** Sí, presente al final.
