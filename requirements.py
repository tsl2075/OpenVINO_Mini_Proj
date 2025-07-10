# Fetch `notebook_utils` module
import requests
from pathlib import Path

if not Path("notebook_utils.py").exists():

    r = requests.get(
        url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py",
    )
    open("notebook_utils.py", "w").write(r.text)

if not Path("cmd_helper.py").exists():
    r = requests.get(
        url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/cmd_helper.py",
    )
    open("cmd_helper.py", "w").write(r.text)

if not Path("pip_helper.py").exists():
    r = requests.get(
        url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/pip_helper.py",
    )
    open("pip_helper.py", "w").write(r.text)

from cmd_helper import clone_repo
from pip_helper import pip_install
import platform

repo_dir = Path("OpenVoice")

clone_repo("https://github.com/myshell-ai/OpenVoice")
orig_english_path = Path("OpenVoice/openvoice/text/_orig_english.py")
english_path = Path("OpenVoice/openvoice/text/english.py")

if not orig_english_path.exists():
    orig_english_path = Path("OpenVoice/openvoice/text/_orig_english.py")
    english_path = Path("OpenVoice/openvoice/text/english.py")

    english_path.rename(orig_english_path)

    with orig_english_path.open("r") as f:
        data = f.read()
        data = data.replace("unidecode", "anyascii")
        with english_path.open("w") as out_f:
            out_f.write(data)


# fix a problem with silero downloading and installing
with Path("OpenVoice/openvoice/se_extractor.py").open("r") as orig_file:
    data = orig_file.read()
    data = data.replace('method="silero"', 'method="silero:3.0"')
    with Path("OpenVoice/openvoice/se_extractor.py").open("w") as out_f:
        out_f.write(data)


pip_install("librosa>=0.8.1", "pydub>=0.25.1", "tqdm", "inflect>=7.0.0", "pypinyin>=0.50.0", "openvino>=2023.3", "gradio>=4.15")
pip_install(
    "--extra-index-url",
    "https://download.pytorch.org/whl/cpu",
    "wavmark>=0.0.3",
    "faster-whisper>=0.9.0",
    "eng_to_ipa>=0.0.2",
    "cn2an>=0.5.22",
    "jieba>=0.42.1",
    "langid>=1.1.6",
    "ipywebrtc",
    "anyascii",
    "torch>=2.1",
    "nncf>=2.11.0",
    "dtw-python",
    "more-itertools",
    "tiktoken",
)
pip_install("--no-deps", "whisper-timestamped>=1.14.2", "openai-whisper")

if platform.system() == "Darwin":
    pip_install("numpy<2.0")