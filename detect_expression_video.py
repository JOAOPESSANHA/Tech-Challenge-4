#Digitar no Terminal do VSCode
# pip install opencv-python-headless deepface tf-keras tqdm deepface
import cv2
from deepface import DeepFace
import os
import numpy as np
from tqdm import tqdm

def detect_emotions(video_path, output_path):
    # Capturar vídeo do arquivo especificado
    cap = cv2.VideoCapture(video_path)

    # Verificar se o vídeo foi aberto corretamente
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    # Obter propriedades do vídeo
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    #inicializar contadores de expressões
   # 
    expressoes = {'angry':0,'disgust':0,'fear':0,'happy':0,'sad':0,'surprise':0,'neutral':0}
    dominant_emotion = ' '
    # Definir o codec e criar o objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para MP4
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Loop para processar cada frame do vídeo
    for _ in tqdm(range(total_frames), desc="Processando vídeo"):
        # Ler um frame do vídeo
        ret, frame = cap.read()

        # Se não conseguiu ler o frame (final do vídeo), sair do loop
        if not ret:
            break

        # Analisar o frame para detectar faces e expressões
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        # Iterar sobre cada face detectada
        for face in result:
            # Obter a caixa delimitadora da face
            x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']
            
            # Obter a emoção dominante
            if face['dominant_emotion'] != dominant_emotion:
                expressoes [face['dominant_emotion']] += 1

            dominant_emotion = face['dominant_emotion']
            
                        
            # Desenhar um retângulo ao redor da face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Escrever a emoção dominante na face
            cv2.putText(frame, dominant_emotion, (x, y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        
        # Escrever o frame processado no vídeo de saída
        out.write(frame)
        

    print('Número de frames examinados:', total_frames)
    print('Número de expressões faciais detectadas:', expressoes)
    
    
    # Liberar a captura de vídeo e fechar todas as janelas
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Caminho para o arquivo de vídeo na mesma pasta do script
script_dir = os.path.dirname(os.path.abspath(__file__))
#Entrar com o nome do arquivo do vídeo a ser processado
input_video_path = 'Unlocking Facial Recognition_ Diverse Activities Analysis.mp4'

#Nome do vídeo de saída
output_video_path = os.path.join(script_dir, 'output_video_Facial_Recognition.mp4')  

# Chamar a função para detectar emoções no vídeo e salvar o vídeo processado
detect_emotions(input_video_path, output_video_path)
