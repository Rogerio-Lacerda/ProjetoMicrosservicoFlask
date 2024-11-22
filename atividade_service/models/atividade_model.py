atividades = [
    {
        'id_atividade': 1,
        'id_disciplina': 1,
        'enunciado': 'Crie um app de todo em Flask',
        'respostas': [
            {'id_aluno': 1, 'resposta': 'todo.py', 'nota': 9},
            {'id_aluno': 2, 'resposta': 'todo.zip.rar'},
            {'id_aluno': 4, 'resposta': 'todo.zip', 'nota': 10}
        ]
    },
    {
        'id_atividade': 2,
        'id_disciplina': 1,
        'enunciado': 'Crie um servidor que envia email em Flask',
        'respostas': [
            {'id_aluno': 4, 'resposta': 'email.zip', 'nota': 10}
        ]
    }
]
class AtividadeNotFound(Exception):
    pass

def listar_atividades():
    return atividades

def obter_atividade(id_atividade):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            return atividade
    raise AtividadeNotFound

estrutura = {
    "id_disciplina": int,
    "enunciado": str,
    "respostas": list
}

def criar_atividades(dados: dict):
    if set(estrutura.keys()) != set(dados.keys()):
        return False

    for key in estrutura:
        if not isinstance(dados[key], estrutura[key]):
            return False

    id = 0
    atividadesList = listar_atividades()
    if(atividades):
        id = atividadesList[-1]['id_atividade'] + 1     
    else:
        id = 1
    dados['id_atividade'] = id

    atividades.append(dados)
    return True

def atualizar_atividades(id_atividade, dados):
    if set(estrutura.keys()) != set(dados.keys()):
        return False

    for key in estrutura:
        if not isinstance(dados[key], estrutura[key]):
            return False
        
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            atividade.update(dados)
            return True
    return False

def deletar_atividades(id_atividade):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            atividades.remove(atividade)
            return True
    raise AtividadeNotFound
    