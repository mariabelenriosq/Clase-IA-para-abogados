import streamlit as st
import datetime

# ==========================================
# CONFIGURACIÓN DE PÁGINA
# ==========================================
st.set_page_config(
    page_title="ArrendaCheck — Validador Jurídico de Canon",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# VALORES DE REFERENCIA DEL IPC (DANE)
# ==========================================
IPC_HISTORICO = {
    "2026 (IPC preliminar / proyectado)": 5.10,
    "2025 (IPC vigencia anterior - DANE 5.20%)": 5.20,
    "2024 (IPC vigencia anterior - DANE 9.28%)": 9.28,
    "2023 (IPC vigencia anterior - DANE 13.12%)": 13.12,
    "Personalizado (ingresar manualmente)": None
}

# ==========================================
# CORPUS JURÍDICO INCORPORADO (Ley 820/2003)
# ==========================================
CORPUS_ARTICULOS = {
    "Artículo 18": (
        "En ningún caso el precio mensual del canon podrá exceder el uno por ciento (1%) "
        "del valor comercial del inmueble o de la parte de él que se dé en arriendo. "
        "La estimación de un valor comercial no podrá exceder el equivalente a dos (2) veces el avalúo catastral vigente."
    ),
    "Artículo 19": (
        "Cuando el canon de arrendamiento se pacte en moneda extranjera, se pagará en moneda legal colombiana "
        "a la tasa de cambio representativa del mercado en la fecha en que fue contraída la obligación."
    ),
    "Artículo 20": (
        "Cada doce (12) meses de ejecución del contrato bajo un mismo precio, el arrendador podrá incrementar el canon "
        "hasta en una proporción que no sea superior al ciento por ciento (100%) del incremento que haya tenido el índice "
        "de precios al consumidor en el año calendario inmediatamente anterior... "
        "El arrendador deberá informarle al arrendatario el monto del incremento y la fecha en que se hará efectivo, "
        "a través del servicio postal autorizado o mediante el mecanismo de notificación personal expresamente pactado."
    )
}

# ==========================================
# ENCABEZADO Y ADVERTENCIA ÉTICA OBLIGATORIA
# ==========================================
st.title("⚖️ ArrendaCheck")
st.caption("Herramienta de análisis jurídico y verificación de cánones de arrendamiento urbano en Colombia")
st.markdown("**Pontificia Universidad Javeriana · Curso: Derecho e Inteligencia Artificial**")

st.warning(
    "⚖️ **ADVERTENCIA LEGAL OBLIGATORIA (Parte 6):** Esta herramienta es un desarrollo académico que no constituye "
    "asesoría jurídica formal ni sustituye la consulta personalizada con un abogado titulado o con un centro de conciliación. "
    "No se almacenan datos personales bajo los términos de la Ley 1581 de 2012."
)

st.divider()

# ==========================================
# MENÚ PRINCIPAL POR PESTAÑAS
# ==========================================
tab_validador, tab_carta, tab_corpus = st.tabs([
    "📊 1. Validador Legal y Calculadora",
    "📝 2. Generador de Objeción Jurídica",
    "📜 3. Corpus Normativo y Preguntas Frecuentes"
])

# ==========================================
# PESTAÑA 1: VALIDADOR Y CALCULADORA
# ==========================================
with tab_validador:
    st.subheader("Verificación de legalidad del incremento")
    
    col_izq, col_der = st.columns([1, 1])

    with col_izq:
        st.markdown("### 📋 Datos del Contrato")
        
        tipo_inmueble = st.radio(
            "Destinación del inmueble arrendado:",
            ["Vivienda Urbana (apartamento, casa, habitación)", "Comercial (local, bodega, oficina)"],
            help="La Ley 820 de 2003 solo regula vivienda urbana. El comercio se rige por el Código de Comercio."
        )

        canon_actual = st.number_input(
            "Canon mensual actual ($ COP):",
            min_value=100000,
            value=1500000,
            step=50000,
            format="%d"
        )

        canon_propuesto = st.number_input(
            "Nuevo canon propuesto / notificado ($ COP):",
            min_value=100000,
            value=1750000,
            step=50000,
            format="%d"
        )

        meses_cumplidos = st.slider(
            "Meses continuos pagando el mismo canon:",
            min_value=1,
            max_value=36,
            value=12,
            help="El artículo 20 de la Ley 820 exige mínimo 12 meses continuos para poder aplicar un reajuste."
        )

        ipc_seleccionado = st.selectbox(
            "Año base de IPC aplicable (DANE):",
            list(IPC_HISTORICO.keys())
        )

        if IPC_HISTORICO[ipc_seleccionado] is None:
            tasa_ipc = st.number_input("Ingresa el % de IPC aplicable:", min_value=0.0, max_value=30.0, value=5.20, step=0.1)
        else:
            tasa_ipc = IPC_HISTORICO[ipc_seleccionado]

        medio_notificacion = st.selectbox(
            "Medio por el cual te notificaron el aumento:",
            [
                "Servicio postal autorizado (correo certificado con acuse de recibo)",
                "Correo electrónico pactado expresamente en el contrato",
                "Mensaje de WhatsApp o chat informal",
                "Aviso verbal o telefónico",
                "Ninguno (me llegó directamente el cobro)"
            ]
        )

        conoce_valor_comercial = st.checkbox("¿Conoces el avalúo catastral o valor comercial del inmueble? (Opcional)")
        valor_comercial = 0
        if conoce_valor_comercial:
            valor_comercial = st.number_input(
                "Valor comercial estimado ($ COP):",
                min_value=0,
                value=150000000,
                step=5000000,
                format="%d"
            )

    with col_der:
        st.markdown("### 🔎 Diagnóstico Jurídico Inmediato")

        if tipo_inmueble.startswith("Comercial"):
            st.error("🚫 **CASO FUERA DE ALCANCE:**")
            st.write(
                "Los inmuebles de destinación comercial (locales, oficinas, bodegas) no están regulados por la Ley 820 de 2003. "
                "En materia comercial impera la autonomía de la voluntad privada y el Código de Comercio. El arrendador y el "
                "arrendatario pueden pactar libremente los incrementos o fijarlos por mutuo acuerdo."
            )
        else:
            # Cálculos matemáticos y jurídicos
            incremento_pesos = canon_propuesto - canon_actual
            incremento_pct = (incremento_pesos / canon_actual) * 100 if canon_actual > 0 else 0
            tope_legal_pesos = canon_actual * (1 + (tasa_ipc / 100))
            sobrecosto_ilegal = max(0.0, canon_propuesto - tope_legal_pesos)

            # Métricas
            m1, m2 = st.columns(2)
            m1.metric("Incremento pretendido", f"{incremento_pct:.2f}%", delta=f"{incremento_pct - tasa_ipc:+.2f}% vs IPC legal", delta_color="inverse")
            m2.metric("Tope legal máximo permitido", f"${tope_legal_pesos:,.0f} COP")

            # Regla 1: Plazo de 12 meses (Art. 20)
            alerta_plazo = meses_cumplidos < 12

            # Regla 2: Porcentaje vs IPC (Art. 20)
            alerta_ipc = incremento_pct > tasa_ipc

            # Regla 3: Tope del 1% del valor comercial (Art. 18)
            alerta_comercial = False
            if valor_comercial > 0:
                tope_1_pct = valor_comercial * 0.01
                if canon_propuesto > tope_1_pct:
                    alerta_comercial = True

            # Regla 4: Formalidad de notificación (Art. 20)
            notificacion_invalida = medio_notificacion in ["Mensaje de WhatsApp o chat informal", "Aviso verbal o telefónico", "Ninguno (me llegó directamente el cobro)"]

            # Veredicto
            if alerta_plazo:
                st.error("❌ **INCREMENTO IMPROCEDENTE POR TIEMPO:**")
                st.write(
                    f"Apenas han transcurrido **{meses_cumplidos} meses** con el canon actual. "
                    "El **artículo 20 de la Ley 820 de 2003** exige expresamente que hayan transcurrido al menos "
                    "**doce (12) meses de ejecución continua bajo un mismo precio** para que el arrendador pueda reajustar el valor."
                )
            elif alerta_ipc:
                st.error("❌ **INCREMENTO ILEGAL POR EXCESO DEL TOPE:**")
                st.write(
                    f"El incremento pretendido es del **{incremento_pct:.2f}%**, superando el tope legal autorizado del **{tasa_ipc:.2f}%** (IPC DANE). "
                    f"Están cobrando **${sobrecosto_ilegal:,.0f} COP** de más cada mes en contravención del **artículo 20 de la Ley 820 de 2003**."
                )
            else:
                st.success("✅ **INCREMENTO PORCENTUAL CONFORME A LA LEY:**")
                st.write(
                    f"El porcentaje cobrado ({incremento_pct:.2f}%) se encuentra dentro del límite máximo autorizado "
                    f"por la ley ({tasa_ipc:.2f}% según IPC del DANE)."
                )

            if alerta_comercial:
                st.error("❌ **VULNERACIÓN DEL ARTÍCULO 18 (TOPE DEL 1%):**")
                st.write(
                    f"El canon de **${canon_propuesto:,.0f} COP** sobrepasa el límite del 1% del valor comercial estimado "
                    f"(${valor_comercial * 0.01:,.0f} COP). La ley prohíbe cánones que superen este umbral."
                )

            if notificacion_invalida:
                st.warning("⚠️ **ALERTA DE INEFICACIA EN LA NOTIFICACIÓN:**")
                st.write(
                    f"La notificación mediante *'{medio_notificacion}'* no cumple con los requisitos del **artículo 20 (inciso 2) de la Ley 820 de 2003**, "
                    "el cual exige que el aviso se remita por servicio postal autorizado o por el medio expresamente pactado en el contrato. "
                    "El arrendatario no está obligado a pagar el reajuste hasta recibir la notificación debida."
                )

# ==========================================
# PESTAÑA 2: GENERADOR DE CARTA DE OBJECIÓN
# ==========================================
with tab_carta:
    st.subheader("Generador de Comunicación Formal de Reclamo")
    st.write("Genera una carta sustentada en la Ley 820 de 2003 para presentar formal y amistosamente a tu arrendador.")

    c1, c2 = st.columns(2)
    with c1:
        nombre_arrendatario = st.text_input("Tu nombre completo (Arrendatario):", value="María Belén Ríos")
        cedula_arrendatario = st.text_input("Número de cédula:", value="1.000.000.000")
        direccion_inmueble = st.text_input("Dirección del inmueble:", value="Calle 100 # 15-20, Apto 402, Bogotá")
    with c2:
        nombre_arrendador = st.text_input("Nombre del arrendador o inmobiliaria:", value="Inmobiliaria Central S.A.S.")
        fecha_carta = st.date_input("Fecha de radicación:", value=datetime.date.today())

    # Generación de la minuta
    modelo_carta = f"""Bogotá D.C., {fecha_carta.strftime('%d de %B de %Y')}

Señores:
{nombre_arrendador}
Ciudad

ASUNTO: Objeción formal al incremento del canon de arrendamiento y solicitud de reajuste conforme a la Ley 820 de 2003
CONTRATO: Arrendamiento de vivienda urbana sobre el inmueble ubicado en {direccion_inmueble}
ARRENDATARIO(A): {nombre_arrendatario}, identificado(a) con C.C. No. {cedula_arrendatario}

Estimados señores:

Por medio de la presente comunicación me dirijo a ustedes de manera respetuosa con el propósito de manifestar mi NO ACEPTACIÓN respecto al incremento en el canon de arrendamiento notificado recientemente para el inmueble de la referencia, con base en las siguientes consideraciones fácticas y jurídicas:

1. FUNDAMENTO JURÍDICO VINCULANTE:
De conformidad con el artículo 20 de la Ley 820 de 2003 (Régimen de Arrendamiento de Vivienda Urbana en Colombia), el arrendador solo puede incrementar el canon tras doce (12) meses continuos de ejecución contractual, y dicho incremento en ningún caso podrá superar el ciento por ciento (100%) de la variación del Índice de Precios al Consumidor (IPC) certificado oficialmente por el DANE para el año calendario inmediatamente anterior.

2. SITUACIÓN PARTICULAR DEL CONTRATO:
El valor que se pretende exigir excede los topes consagrados por el legislador y/o no ha cumplido con los presupuestos temporales y de notificación formal por servicio postal autorizado previstos en el articulado citado. Así mismo, el artículo 18 de la misma normativa dispone que el canon mensual no podrá en ningún caso ser superior al uno por ciento (1%) del valor comercial del inmueble.

3. SOLICITUD:
En virtud del principio de buena fe contractual y acatamiento normativo, solicito comedidamente:
a) Liquidar el canon mensual ajustándolo estrictamente al tope máximo legal autorizado por el IPC del DANE para vivienda urbana.
b) Emitir la respectiva cuenta de cobro corregida con el valor exacto de ley para efectuar el pago oportuno de las obligaciones causadas.

Quedo atento(a) a recibir su pronta respuesta a través de los canales pactados en el contrato.

Cordialmente,


_____________________________________________
{nombre_arrendatario}
C.C. No. {cedula_arrendatario}
Arrendatario(a)
"""

    st.text_area("Borrador generado:", modelo_carta, height=350)
    st.download_button(
        label="📥 Descargar carta en formato texto (.txt)",
        data=modelo_carta,
        file_name="carta_objecion_arrendamiento.txt",
        mime="text/plain"
    )

# ==========================================
# PESTAÑA 3: CORPUS NORMATIVO Y FAQ
# ==========================================
with tab_corpus:
    st.subheader("Corpus Normativo — Ley 820 de 2003")
    st.write("Consulta directamente los artículos que blindan las respuestas de ArrendaCheck contra alucinaciones:")

    for art, texto in CORPUS_ARTICULOS.items():
        with st.expander(f"📖 {art}"):
            st.info(texto)

    st.divider()
    st.subheader("Preguntas Frecuentes de Arrendatarios")
    
    with st.expander("¿El arrendador me puede subir el arriendo dos veces en el mismo año?"):
        st.write("No. El artículo 20 de la Ley 820 de 2003 establece que los reajustes solo proceden **cada doce (12) meses** de ejecución continua bajo un mismo precio.")

    with st.expander("¿Me pueden subir el arriendo por WhatsApp?"):
        st.write("El artículo 20 exige comunicación escrita por **servicio postal autorizado** o el medio expresamente pactado en el contrato de arrendamiento. Si no se pactó WhatsApp en el contrato, la notificación carece de eficacia legal plena.")

    with st.expander("¿Aplica este límite para un local comercial o consultorio?"):
        st.write("No. La Ley 820 de 2003 protege exclusivamente la **vivienda urbana**. Los locales comerciales se rigen por el Código de Comercio y la autonomía de la voluntad.")
