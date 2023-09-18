import gradio as gr
import openai
openai.api_key ="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"

start_sequence = "\nAI:"
restart_sequence = "\nHUman"

prompt = "The following is a conservation with an AI assistant. the asssistant is helpful, creative,clever,and very friendly.\n\Human:Hello,who are you?\nAI: I am an AI created by openAI.How can I help you today?\nHuman: "
def gpt_output(prompt):
     response  = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1,
        frequency_penalty= 0,
        presence_penalty= 0.6,
        stop=[" Human:"," AI:"]
    )
     print(response.choices[0].text)


     return response.choices[0].text

# while True:
# query = input("Ask a Question to AI:\n")
# gpt_output(query)
def AGI_bot(input,history):
    history = history or []
    s = list(sum(history,()))
    s.append(input)
    inp = ''.join(s)
    output = gpt_output(inp)
    history.append((input,output))
    return  history,history

block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>AGI AI Assistant</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(AGI_bot,inputs=[message,state],outputs=[chatbot,state])

block.launch(debug=True)


