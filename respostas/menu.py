from classes import *

def exibir_menu():
  print("\nMenu:")
  print("1. Adicionar Disciplina")
  print("2. Adicionar Atividade")
  print("3. Marcar Atividade como Concluída")
  print("4. Listar Atividades em Aberto e Concluídas")
  print("5. Sair")


disciplinas = []

while True:
  exibir_menu()
  escolha = input("Escolha uma opção: ")

  if escolha == "1":
      nome_disciplina = input("Digite o nome da disciplina: ")
      disciplina = Disciplina(nome_disciplina)
      disciplinas.append(disciplina)
      print(f"Disciplina '{nome_disciplina}' adicionada com sucesso.")

  elif escolha == "2":
      if not disciplinas:
          print("Não há disciplinas para adicionar atividades. Crie uma disciplina primeiro.")
      else:
          print("Escolha a disciplina para adicionar a atividade:")
          for i, disciplina in enumerate(disciplinas, 1):
              print(f"{i}. {disciplina.nome}")
          escolha_disciplina = int(input("Digite o número da disciplina: "))

          if 1 <= escolha_disciplina <= len(disciplinas):
              disciplina = disciplinas[escolha_disciplina - 1]
              nome_atividade = input("Digite o nome da atividade: ")
              data_atividade = input("Digite a data da atividade: ")
              disciplina.adicionar_atividade(nome_atividade, data_atividade)
              print(f"Atividade '{nome_atividade}' adicionada para a disciplina '{disciplina.nome}'.")

  elif escolha == "3":
      if not disciplinas:
          print("Não há disciplinas para marcar atividades como concluídas.")
      else:
          print("Escolha a disciplina para marcar a atividade como concluída:")
          for i, disciplina in enumerate(disciplinas, 1):
              print(f"{i}. {disciplina.nome}")
          escolha_disciplina = int(input("Digite o número da disciplina: "))

          if 1 <= escolha_disciplina <= len(disciplinas):
              disciplina = disciplinas[escolha_disciplina - 1]
              listar_atividades_disciplina(disciplina)

              if disciplina.atividades:
                  escolha_atividade = int(input("Digite o número da atividade a ser marcada como concluída: "))
                  if 1 <= escolha_atividade <= len(disciplina.atividades):
                      atividade = disciplina.atividades[escolha_atividade - 1]
                      atividade.marcar_como_concluida()
                      print(f"Atividade '{atividade.nome}' marcada como concluída.")
                  else:
                      print("Opção inválida.")

  elif escolha == "4":
      if not disciplinas:
          print("Não há disciplinas para listar atividades.")
      else:
          print("Escolha a disciplina para listar atividades em aberto e concluídas:")
          for i, disciplina in enumerate(disciplinas, 1):
              print(f"{i}. {disciplina.nome}")
          escolha_disciplina = int(input("Digite o número da disciplina: "))

          if 1 <= escolha_disciplina <= len(disciplinas):
              disciplina = disciplinas[escolha_disciplina - 1]
              listar_atividades_disciplina(disciplina)
          else:
              print("Opção inválida.")

  elif escolha == "5":
      break

  else:
      print("Opção inválida. Tente novamente.")
