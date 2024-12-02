# Tech-Challenge-4
Trabalho do curso IA para DEVs - Grupo 5

O presente trabalho é a proposta de solução do Grupo 5 para o Tech Challenge da Fase 4 - Análise de Dados do curso IA para Devs 
que consiste em utilizar as técnicas de reconhecimento facial, análise de expressões emocionais em vídeos e detecção de atividades, a partir do vídeo fornecido para o exercício.
Assim, o código irá ler o arquivo "Unlocking Facial Recognition_ Diverse Activities Analysis.mp4", que deve estar presente no diretório do projeto e, a partir dele, efetuar a execução do código 'detect_expression_video.py' que irá gerar a marcação e classificação das faces mostradas no vídeo de entrada.
Para tanto, é necessário digitar os seguintes comandos, utilizando o terminal do VSCode, para executar o projeto:

Terminal>pip install opencv-python-headless deepface tf-keras tqdm deepface

Terminal>python ./detect_expression_video.py

Como saída, teremos um resumo dos contadores de expressões detectadas no vídeo de entrada, bem como o arquivo "output_video_Facial_Recognition.mp4" mostrando as faces detectadas, dentro de retângulos verdes e suas respectivas classificações. Esse arquivo servirá para verificar a precisão de detecção das faces e emoções.

Em seguida, utilizando como entrada o mesmo arquivo "Unlocking Facial Recognition_ Diverse Activities Analysis", o código reabre o arquivo de entrada e efetua a detecção de poses, com a impressão de pontos de marcação ("Landmarks") que serão utilizados para classificar os movimentos escolhidos. Como saída, o programa imprime o número de repetições do movimento escolhido detectado no arquivo de entrada e grava um outro vídeo mostrando as marcações (Landmarks) desenhadas no vídeo (output_video_braco_esquerdo_levantado.mp4).

No caso, escolhemos o movimento de levantar o braço esquerdo (left arm up) que aparece na maioria das cenas do vídeo de entrada. Sua execução é iniciada pelo comando no terminal do VSCode:

Terminal>pip install opencv-python mediapipe tf-keras tqdm

Terminal>python pose_detection_arm_up

