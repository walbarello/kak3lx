Script Automático com Barra de Progresso
Este é um script em Python com interface gráfica usando a biblioteca Tkinter. O script realiza a automação de pressionamento de teclas, incluindo a tecla 'X', com a capacidade de configurar diferentes atrasos entre letras, atrasos para a tecla 'X' e duração do pressionamento da tecla 'X'. Além disso, o script apresenta uma barra de progresso para visualizar o andamento do ciclo.

Requisitos
Python 3.x
Biblioteca pynput (instalável com pip install pynput)
Utilização
Execute o script em um ambiente Python 3.x.

Preencha os campos na interface gráfica:

Letras (separadas por vírgula): Letras que serão pressionadas.
Atraso entre letras (segundos): Tempo de espera entre cada pressionamento de letra.
Atraso para 'X' (segundos): Tempo de espera antes de pressionar a tecla 'X'.
Duração do pressionamento de 'X' (segundos): Tempo que a tecla 'X' será mantida pressionada.
Atraso entre ciclos (segundos): Tempo de espera entre cada ciclo completo.
Clique no botão "Iniciar" para começar a execução do script.

Se necessário, clique no botão "Parar" para interromper a execução do script.

Observação: Durante a execução do script, os campos de entrada são desativados para evitar alterações enquanto o script está em andamento.

Personalização
Você pode personalizar o script ajustando os valores padrão nos campos de entrada ou modificando a lógica do script conforme necessário.

Lógica do Script
press_keys_once(keys, delay): Função que pressiona e libera as teclas especificadas com um atraso entre elas.
start_script(): Função que inicia a execução do script em uma thread separada.
run_script(): Função principal que contém a lógica do script, incluindo a barra de progresso.
stop_script(): Função para interromper a execução do script.
set_entry_state(state): Função para ativar ou desativar os campos de entrada com base no estado fornecido.
Barra de Progresso
A barra de progresso é implementada usando ttk.Progressbar e é atualizada dinamicamente durante a execução do script para refletir o andamento do ciclo.

Personalização Adicional
Sinta-se à vontade para personalizar o script conforme necessário para atender aos requisitos específicos do seu caso de uso.






