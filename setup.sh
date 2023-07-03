#Update packages
sudo apt-get update
sudo apt-get upgrade -y

#setup development environment
sudo apt-get install -y zsh
sudo chsh -s /usr/bin/zsh

cd ~/
git clone https://github.com/jtvana/dotfiles.git
mv dotfiles/.??* ~/
echo "export LD_LIBRARY_PATH=/usr/lib/wsl/lib:\$LD_LIBRARY_PATH" >> ~/.zshrc

# Setting up CUDA drivers
cd ~/
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
sudo sh cuda_11.8.0_520.61.05_linux.run --toolkit --silent
rm cuda_11.8.0_520.61.05_linux.run

echo "If you can see your GPU listed below, everything went smoothly so far:"
nvidia-smi

sudo apt-get install -y python3-pip
# Installing pytorch utilities
echo "Install pytorch built with cuda 11.8 via pip3 install"
python3 -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

#installing OpenAI python libs
python3 -m pip install openai

