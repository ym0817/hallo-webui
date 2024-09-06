@echo off

echo clone models
git lfs install
git clone https://huggingface.co/fudan-generative-ai/hallo pretrained_models
curl -L -o pretrained_models/hallo/net.pth https://huggingface.co/fudan-generative-ai/hallo/resolve/main/hallo/net.pth?download=true

echo Install Depends
python -m venv venv
call venv/scripts/activate
pip install -r requirements.txt
pip install -e . 

pip install bitsandbytes-windows --force-reinstall

echo Install GPU libs
pip install torch==2.2.2+cu121 torchaudio torchvision --index-url https://download.pytorch.org/whl/cu121

echo install complete
pause