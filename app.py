from flask import Flask, render_template, request
import openai

# initialize the Flask app
app = Flask(__name__)

# set the API key for the OpenAI API
openai.api_key = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/response", methods=["POST"])
def response():
    user_input = request.form["user_input"]
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    return response

if __name__ == "__main__":
    app.run(debug=True)
