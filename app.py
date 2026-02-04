import streamlit as st
import random

st.set_page_config(page_title="Cronograma Escolar")

st.title("📚 Gerador de Cronograma Escolar")

DIAS = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
HORARIOS_POR_DIA = 6

TURMAS = [
    "1A", "1B", "1C", "1D",
    "2A", "2B", "2C", "2D",
    "3A", "3B", "3C", "3D"
]

st.subheader("Cadastro das matérias")

qtd_materias = st.number_input(
    "Quantas matérias existem?",
    min_value=1,
    step=1
)

materias = {}

for i in range(int(qtd_materias)):
    with st.expander(f"Matéria {i+1}"):
        nome = st.text_input("Nome da matéria", key=f"m{i}")
        professor = st.text_input("Professor", key=f"p{i}")
        aulas = st.number_input(
            "Aulas semanais",
            min_value=1,
            max_value=30,
            step=1,
            key=f"a{i}"
        )

        if nome:
            materias[nome.upper()] = {
                "professor": professor,
                "aulas": aulas
            }

def gerar_cronograma(materias):
    cronogramas = {}

    for turma in TURMAS:
        cronograma = {dia: [] for dia in DIAS}
        lista = []

        for materia, dados in materias.items():
            for _ in range(dados["aulas"]):
                lista.append(f"{materia} ({dados['professor']})")

        total = len(DIAS) * HORARIOS_POR_DIA
        while len(lista) < total:
            lista.append("Livre")

        random.shuffle(lista)

        i = 0
        for dia in DIAS:
            for _ in range(HORARIOS_POR_DIA):
                cronograma[dia].append(lista[i])
                i += 1

        cronogramas[turma] = cronograma

    return cronogramas

if st.button("Gerar cronograma"):
    if not materias:
        st.warning("Cadastre pelo menos uma matéria.")
    else:
        resultado = gerar_cronograma(materias)

        for turma, cronograma in resultado.items():
            st.subheader(f"Turma {turma}")
            st.table(cronograma)
