from PySimpleGUI import PySimpleGUI as sg 

sg.theme('Reddit')

layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Me manter conectado')],
    [sg.Button('Entrar')]
]

window = sg.Window('ENGSOFT', layout)

while True:
    eventos, valores = window.read()
    if eventos == sg.WINDOW_CLOSED: 
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'gabriel' and valores['senha'] == '123456':
            print('Bem-vindo ao meu aplicativo')
        else:
            print('Acesso negado!')
            print('Usuário não autorizado...')