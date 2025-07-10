import gradio as gr

def gradio_ui():
    with gr.Blocks() as block:
        gr.HTML(
            f"""
            <h1 style='text-align: center;'> Magic 8 Ball 🎱 </h1>
            <h3 style='text-align: center;'> Ask a question and receive wisdom </h3>
            <p style='text-align: center;'> Powered by <a href="https://github.com/huggingface/parler-tts"> Parler-TTS</a>
            """
        )
        with gr.Group():
            with gr.Row():
                audio_out = gr.Audio(label="Spoken Answer", streaming=True, autoplay=True)
                answer = gr.Textbox(label="Answer")
                state = gr.State()
            with gr.Row():
                audio_in = gr.Audio(label="Speak your question", sources="microphone", type="filepath")

    return block
    # block.launch()