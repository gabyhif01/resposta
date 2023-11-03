class Professor:
  def __init__(self, nome):
      self.nome = nome
      self.disciplinas = []

  def adicionar_disciplina(self, disciplina):
      self.disciplinas.append(disciplina)

  def listar_disciplinas(self):
      print(f"Professor {self.nome} ensina as seguintes disciplinas:")
      for disciplina in self.disciplinas:
          print(disciplina.nome)

class Disciplina:
  def __init__(self, nome):
      self.nome = nome
      self.atividades = []

  def adicionar_atividade(self, nome_atividade, data):
      atividade = Atividade(nome_atividade, data)
      self.atividades.append(atividade)

  def listar_atividades(self):
      print(f"Atividades da disciplina {self.nome}:")
      for atividade in self.atividades:
          print(f"{atividade.data}: {atividade.nome}")

class Atividade:
  def __init__(self, nome, data):
      self.nome = nome
      self.data = data
      self.concluida = False

  def marcar_como_concluida(self):
      self.concluida = True

  def esta_concluida(self):
      return self.concluida

def listar_atividades_disciplina(disciplina):
  atividades_em_aberto = []
  atividades_concluidas = []
  for atividade in disciplina.atividades:
      if atividade.esta_concluida():
          atividades_concluidas.append(atividade)
      else:
          atividades_em_aberto.append(atividade)

  print("Atividades em aberto:")
  for atividade in atividades_em_aberto:
      print(f"{atividade.data}: {atividade.nome}")

  print("\nAtividades concluídas:")
  for atividade in atividades_concluidas:
      print(f"{atividade.data}: {atividade.nome}")