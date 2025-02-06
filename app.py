from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from ultralytics import YOLO
import base64
import io

app = Flask(__name__)

# Carregar o modelo YOLOv8
model = YOLO("yolo-Weights/yolov8n.pt")

# Classe para as imagens processadas
processed_images = []

# Classes do YOLO traduzidas para português
classNames = [
    "pessoa", "bicicleta", "carro", "moto", "avião", "ônibus", "trem", "caminhão", "barco",
    "semáforo", "hidrante", "sinal de parada", "parquímetro", "banco", "pássaro", "gato",
    "cachorro", "cavalo", "ovelha", "vaca", "elefante", "urso", "zebra", "girafa", "mochila",
    "guarda-chuva", "bolsa", "gravata", "mala", "frisbee", "esquis", "snowboard", "bola esportiva",
    "pipa", "bastão de beisebol", "luva de beisebol", "skate", "prancha de surf", "raquete de tênis",
    "garrafa", "taça de vinho", "copo", "garfo", "faca", "colher", "tigela", "banana", "maçã",
    "sanduíche", "laranja", "brócolis", "cenoura", "hot dog", "pizza", "donut", "bolo", "cadeira",
    "sofá", "planta em vaso", "cama", "mesa de jantar", "toalete", "monitor de TV", "laptop", "mouse",
    "controle remoto", "teclado", "celular", "micro-ondas", "forno", "torradeira", "pia", "geladeira",
    "livro", "relógio", "vaso", "tesoura", "urso de pelúcia", "secador de cabelo", "escova de dentes"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        data = request.json['image']
        image_bytes = base64.b64decode(data.split(',')[1])  # Decodifica a imagem Base64
        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)  # Converte para OpenCV
        
        # Processar com YOLO
        results = model(image)
        detected_objects = []

        for r in results:
            for box in r.boxes:
                confidence = float(box.conf[0])
                if confidence >= 0.5:  # Ajuste o threshold conforme necessário
                    cls = int(box.cls[0])
                    object_name = classNames[cls]
                    detected_objects.append(object_name)

                    # Desenha retângulo e rótulo na imagem
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    cv2.putText(image, f'{object_name} {confidence:.2f}', (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Codifica a imagem processada para Base64 e armazena
        _, buffer = cv2.imencode('.jpg', image)
        processed_image = base64.b64encode(buffer).decode('utf-8')
        processed_images.append(f"data:image/jpeg;base64,{processed_image}")

        # Retorna apenas os objetos detectados
        return jsonify({"objects": detected_objects})

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/detected-images')
def detected_images():
    return render_template('detected_images.html', images=processed_images)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
