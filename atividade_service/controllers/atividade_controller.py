from flask import Blueprint, request, jsonify
from models import atividade_model
from clients.pessoa_service_client import PessoaServiceClient

atividade_bp = Blueprint('atividade_bp', __name__)

@atividade_bp.route('/', methods=['GET'])
def listar_atividades():
    atividades = atividade_model.listar_atividades()
    return jsonify(atividades)

@atividade_bp.route('/<int:id_atividade>', methods=['GET'])
def obter_atividade(id_atividade):
    try:
        atividade = atividade_model.obter_atividade(id_atividade)
        return jsonify(atividade)
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

@atividade_bp.route('/<int:id_atividade>/professor/<int:id_professor>', methods=['GET'])
def obter_atividade_para_professor(id_atividade, id_professor):
    try:
        atividade = atividade_model.obter_atividade(id_atividade)
        if not PessoaServiceClient.verificar_leciona(id_professor, atividade['id_disciplina']):
            atividade = atividade.copy()
            atividade.pop('respostas', None)
        return jsonify(atividade)
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

@atividade_bp.route('/', methods=['POST'])
def criar_atividade():
    try:
        dados = request.get_json()
        atividade = atividade_model.criar_atividades(dados)
        if not atividade: 
            raise atividade_model.AtividadeNotFound
        return jsonify({'sucesso': 'Atividade criada com sucesso'}), 201
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Dados inválidos para criação'}), 400

@atividade_bp.route('/<int:id_atividade>', methods=['PUT'])
def atualizar_atividade(id_atividade):
    try:
        dados = request.get_json()
        atividade = atividade_model.atualizar_atividades(id_atividade, dados)
        if not atividade: 
            raise atividade_model.AtividadeNotFound
        return jsonify({'sucesso': 'Atividade alterada com sucesso'}), 200
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada ou dados inválidos para alteração'}), 404
    
@atividade_bp.route('/<int:id_atividade>', methods=['DELETE'])
def deletar_atividade(id_atividade):
    try:
        atividade = atividade_model.deletar_atividades(id_atividade)
        if not atividade: 
            raise atividade_model.AtividadeNotFound
        return jsonify({'sucesso': 'Atividade deletada com sucesso'}), 200
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    
    


