# Tech-Challenge-4
Trabalho do curso IA para DEVs - Grupo 5

O presente trabalho é a proposta de solução do Grupo 5 para o Tech Challenge da Fase 4 - Análise de Dados do curso IA para Devs 
que consiste em utilizar as técnicas de reconhecimento facial, análise de expressões emocionais em vídeos e detecção de atividades, a partir do vídeo fornecido para o exercício.
Assim, o código irá ler o arquivo "Unlocking Facial Recognition_ Diverse Activities Analysis", que deve estar presente no diretório do projeto e, a partir dele, efetuar a execução do código 'detect_expression_video.py' que irá gerar a marcação e classificação das faces mostradas no vídeo de entrada.
Para tanto, é necessário digitar os seguintes comandos, utilizando o terminal do VSCode, para executar o projeto:

Terminal>pip install opencv-python-headless deepface tf-keras tqdm deepface

Terminal>python ./detect_expression_video.py

Como saída, teremos um resumo dos contadores de expressões detectadas no vídeo de entrada, bem como o arquivo output_video_Facial_Recognition.mp4 mostrando as faces detectadas, dentro de retângulos verdes e suas respectivas classificações.
Em seguida, 
