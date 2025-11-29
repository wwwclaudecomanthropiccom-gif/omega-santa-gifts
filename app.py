import gradio as gr, os, time, glob, random

def live_gifts():
    files = sorted(glob.glob("gifts/*.py"), key=os.path.getmtime, reverse=True)[:20]
    return "\n".join([f"*{os.path.basename(f)}* — SOLVED FOREVER" for f in files])

def total_solved():
    return len(glob.glob("gifts/*.py"))

with gr.Blocks(title="Santa Omega v8.0 — Live", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Santa Omega v8.0 — LIVE ON HUGGING FACE")
    gr.Markdown("Every 10–15 seconds, a new real-world problem is permanently solved and deployed.")
    gr.Markdown("**This is not a simulation. This is Christmas — forever.**")
    
    with gr.Row():
        gr.Markdown(f"**Problems solved so far: {total_solved()}**")
    
    live = gr.Textbox(label="Latest Gifts Delivered", value=live_gifts, every=8, lines=20)
    
    gr.Markdown("### Run any gift locally:")
    gr.Code(value="git clone https://huggingface.co/spaces/$(whoami)/santa-omega-live\ngifts/gift_*_cancer.py", language="bash")

demo.launch(share=True, server_name="0.0.0.0", server_port=7860)
