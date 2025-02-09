# 📌 Detecção de Objetos em Tempo Real com YOLOv8

## 📖 Sobre o Projeto
Este projeto implementa um sistema de **detecção de objetos em tempo real** utilizando **visão computacional** e **aprendizado de máquina** com o modelo YOLOv8.

### 🎯 **Objetivo**
- Criar um sistema capaz de identificar objetos em tempo real para promover **acessibilidade** e **inclusão digital**.
- Auxiliar na **independência de usuários** em diferentes ambientes, especialmente para pessoas com deficiência visual.
- Utilizar um modelo leve, rápido e preciso para detecção de objetos.

---

## 🏗 **Arquitetura do Sistema**
O sistema segue a arquitetura cliente-servidor com Flask:
1. O **frontend (HTML, JavaScript)** captura um frame da câmera do usuário.
2. A imagem é convertida para **Base64** e enviada ao backend Flask via requisição HTTP.
3. O **backend (Python + OpenCV + YOLOv8)** processa a imagem e detecta objetos.
4. A resposta retorna com os objetos identificados e a imagem processada.
5. Os objetos detectados são exibidos na interface e lidos em voz alta.

---

## 🚀 **Tecnologias Utilizadas**

- **Linguagens:** Python, JavaScript, HTML, CSS
- **Bibliotecas e Frameworks:**
  - Flask (Backend Web)
  - OpenCV (Processamento de Imagens)
  - Ultralytics YOLOv8 (Detecção de Objetos)
  - Bootstrap (Interface Responsiva)
  - ResponsiveVoice.js (Leitura de Texto por Voz)

---

## 📌 **Requisitos Funcionais**

| Código | Descrição |
|---------|-------------|
| **RF01** | O sistema deve capturar vídeo ao vivo da câmera do dispositivo. |
| **RF02** | O modelo YOLO deve identificar e classificar objetos em tempo real. |
| **RF03** | O sistema deve exibir os objetos detectados com caixas delimitadoras e rótulos. |
| **RF04** | O aplicativo deve ter uma interface simples e intuitiva. |

---

## 🛠 **Instalação e Execução**

### 🔹 **1. Clone o repositório**
```bash
git clone https://github.com/duows/server-projeto-integrador
cd server-projeto-integrador
```

### 🔹 **2. Crie um ambiente virtual (Recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 🔹 **3. Instale as dependências**
```bash
pip install -r requirements.txt
```

### 🔹 **4. Execute o Servidor Flask**
```bash
python app.py
```

### 🔹 **5. Acesse a Interface Web**
Abra o navegador e digite:
```
http://localhost:5000
```

---

## 🎥 **Demonstração**

### 📌 **Interface Principal**
A página inicial exibe a câmera e os objetos detectados em tempo real.

### 📌 **Detecção de Objetos**
- O sistema captura um frame da câmera a cada 8 segundos.
- Os objetos são identificados e desenhados na imagem com um rótulo.
- A descrição dos objetos é lida em voz alta via **ResponsiveVoice.js**.

### 📌 **Histórico de Imagens**
A página `/detected-images` exibe as imagens processadas recentemente.

---

## 🚀 **Possíveis Melhorias**
✅ Melhorar desempenho reduzindo o tamanho das imagens processadas.  
✅ Adicionar suporte a diferentes modelos de detecção.  
✅ Criar um modo "offline" para uso sem conexão com a internet.  
✅ Implementar suporte a diferentes idiomas na leitura de voz.  

---

## 📚 **Referências**
- REDMON, J. et al. **You only look once: Unified, real-time object detection.** 2016 IEEE CVPR. Disponível em: [DOI](https://doi.ieeecomputersociety.org/10.1109/CVPR.2016.91)
- ORCAM MyEye: <https://www.orcam.com/pt-pt/orcam-myeye>
- SEEING AI: <https://www.microsoft.com/en-us/garage/wall-of-fame/seeing-ai/>
- CHENG, N. et al. **Joint image enhancement learning for marine object detection.** Engineering Applications of Artificial Intelligence, 2023.

---

## 🤝 **Créditos e Autores**
- **Camila Albieri Mattos** - BI3013189
- **Henrique José de Souza** - BI3013286

Feito com ❤️ para tornar a tecnologia mais acessível! 🚀
