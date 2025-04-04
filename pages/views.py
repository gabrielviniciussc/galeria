from django.shortcuts import render

# Função para exibir a página inicial
def home(request):
    # Aqui você pode passar uma lista de fotos ou outros dados
    fotos = ['foto1.jpg', 'foto2.jpg', 'foto3.jpg']  # Exemplo de fotos
    return render(request, 'pages/home.html', {'fotos': fotos})

# Função para exibir a página sobre
def about(request):
    return render(request, 'pages/about.html')
