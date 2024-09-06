import sys
import gradio as gr
import subprocess
from datetime import datetime
import os
import platform

def generate_video(ref_img, ref_audio,settings_face_expand_ratio=1.2, setting_steps=40, setting_cfg=3.5, settings_seed=42, settings_fps=25, settings_motion_pose_scale=1.1, settings_motion_face_scale=1.1, settings_motion_lip_scale=1.1, settings_n_motion_frames=2, settings_n_sample_frames=16):
    # Ensure file paths are correct
    if not os.path.isfile(ref_img) or not os.path.isfile(ref_audio):
        return "Error: File not found", None

    # Path to the output video file
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    # Check if output exists and if not create it
    if not os.path.exists("output"):
        os.makedirs("output")

    output_video = f"output/{timestamp}.mp4"

    # Determine the command based on the operating system
    if platform.system() == "Windows":
        command = [
            "venv\\Scripts\\python.exe",
            "scripts\\inference.py",
            "--source_image", ref_img,
            "--driving_audio", ref_audio,
            "--output", output_video,
            "--face_expand_ratio", str(settings_face_expand_ratio),
            "--setting_steps", str(setting_steps),
            "--setting_cfg", str(setting_cfg),
            "--settings_seed", str(settings_seed),
            "--settings_fps", str(settings_fps),
            "--settings_motion_pose_scale", str(settings_motion_pose_scale),
            "--settings_motion_face_scale", str(settings_motion_face_scale),
            "--settings_motion_lip_scale", str(settings_motion_lip_scale),
            "--settings_n_motion_frames", str(settings_n_motion_frames),
            "--settings_n_sample_frames", str(settings_n_sample_frames)
        ]
    else:
        command = [
            "python3",
            "scripts/inference.py",
            "--source_image", ref_img,
            "--driving_audio", ref_audio,
            "--output", output_video,
            "--setting_steps", str(setting_steps),
            "--setting_cfg", str(setting_cfg),
            "--settings_seed", str(settings_seed),
            "--settings_fps", str(settings_fps),
            "--settings_motion_pose_scale", str(settings_motion_pose_scale),
            "--settings_motion_face_scale", str(settings_motion_face_scale),
            "--settings_motion_lip_scale", str(settings_motion_lip_scale),
            "--settings_n_motion_frames", str(settings_n_motion_frames),
            "--settings_n_sample_frames", str(settings_n_sample_frames)
        ]

    try:
        # Execute the command
        result = subprocess.run(command, check=True)

        if result.returncode == 0:
            return "Video generated successfully", output_video
        else:
            return "Error generating video", None

    except subprocess.CalledProcessError as e:
        return f"Error: {str(e)}", None


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            ref_img = gr.Image(label="Reference Image", type="filepath")
            ref_audio = gr.Audio(label="Audio", type="filepath")
            with gr.Accordion("Settings", open=True):
                settings_face_expand_ratio = gr.Slider(label="Face Expand Ratio", value=1.2, minimum=0, maximum=10, step=0.01)
                setting_steps = gr.Slider(label="Steps", value=40, minimum=1, maximum=200, step=1)
                setting_cfg = gr.Slider(label="CFG Scale", value=3.5, minimum=0, maximum=10, step=0.01)
                settings_seed = gr.Textbox(label="Seed", value=42)
                settings_fps = gr.Slider(label="FPS", value=25, minimum=1, maximum=200, step=1)
                with gr.Accordion("Motion Scale", open=True):
                    settings_motion_pose_scale = gr.Slider(label="Motion Pose Scale", value=1.0, minimum=0, maximum=5, step=0.01)
                    settings_motion_face_scale = gr.Slider(label="Motion Face Scale", value=1.0, minimum=0, maximum=5, step=0.01)
                    settings_motion_lip_scale = gr.Slider(label="Motion Lip Scale", value=1.0, minimum=0, maximum=5, step=0.01)
                with gr.Accordion("Extra Settings", open=True):
                    settings_n_motion_frames = gr.Slider(label="N Motion Frames", value=2, minimum=1, maximum=100, step=1)
                    settings_n_sample_frames = gr.Slider(label="N Sample Frames", value=16, minimum=1, maximum=100, step=1)
        with gr.Column():
            result_status = gr.Label(value="Status")
            result_video = gr.Video(label="Result Video", interactive=False)
            result_btn = gr.Button(value="Generate Video")

    result_btn.click(fn=generate_video, inputs=[ref_img, ref_audio,settings_face_expand_ratio, setting_steps, setting_cfg, settings_seed, settings_fps, settings_motion_pose_scale, settings_motion_face_scale, settings_motion_lip_scale, settings_n_motion_frames, settings_n_sample_frames], outputs=[result_status, result_video])

if __name__ == "__main__":
    share_url = False if "--share" not in sys.argv else True

    demo.queue()
    demo.launch(inbrowser=True, share=share_url)

