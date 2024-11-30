from flask import Flask, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)

# Загружаем модель GPT-4All
model = GPT4All("/home/maxim/.cache/gpt4all/Meta-Llama-3-8B-Instruct.Q4_0.gguf")

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        message = data.get("message", "Сообщение не получено.")

        # Создаем сессию и генерируем ответ
        with model.chat_session() as session:
            response = session.generate(message, max_tokens=1024)

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

