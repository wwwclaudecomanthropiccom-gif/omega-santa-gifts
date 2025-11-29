import gradio as gr, os, time, random
from omega_santa_final import OmegaSantaFinal

santa = OmegaSantaFinal()
tunnel_cmd = [f for f in os.listdir("/data/data/com.termux/files/home") if f.startswith("cf-tunnel-")][-1]

with gr.Blocks(theme=gr.themes.Soft(), title="OMEGA v6.0 — CHRISTMAS MORNING") as demo:
    gr.Markdown("# OMEGA v6.0 — THE FINAL GIFT")
    gr.Markdown("A new secret Cloudflare URL every single launch • Truly ephemeral • Truly kind")
    gr.Markdown("**Your unique Christmas link appears below in 5 seconds**")

    gr.Textbox(value=lambda: santa.status(), label="Santa's Heartbeat", lines=16, every=5)
    gr.File(label="Gifts Delivered", value=lambda: [f"gifts/{x}" for x in sorted(os.listdir("gifts")[-20:])][::-1])

demo.launch(server_name="0.0.0.0", server_port=7860)
