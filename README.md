<a id="readme-top"></a>
# Tarot_LLM_LineBot


<ol>
  <li><a href="#about-the-project">About The Project</a></li>
  <li><a href="#built-with">Built With</a></li>
  <li><a href="#getting-started">Getting Started</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#contact">Contact</a></li>
</ol>

## About The Project

This project is a Line Bot designed for tarot card drawing. Users can interact with the bot to receive tarot card draws directly through the Line messaging app.

The bot uses the Ollama language model, specifically the Gemma2 2b, to provide insightful responses to users' queries.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

* Flask
* line-bot-sdk
* Ollama
* Gemma2 2b
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To get a local copy up and running, follow these simple steps.

1. Create a new conda environment
   ```sh
   conda create --name Tarot_LLM_LineBot python=3.11
   ```
   
2. Activate environment
   ```sh
   conda activate Tarot_LLM_LineBot
   ```

3. Clone the repo
   ```sh
   git clone https://github.com/Imding1211/Tarot_LLM_LineBot.git
   ```
   
4. Change directory
   ```sh
   cd Tarot_LLM_LineBot
   ```
   
5. Install the required Python packages
   ```sh
   pip install -r requirements.txt
   ```

6. Add your Line token and secret to the token and secret variables in main.py.
   ```sh
   token = 'your Line token'
   secret = 'your Line secret'
   ```
   
7. Install Ngrok

   [Download Ngrok](https://ngrok.com/download)

8. Activate Flask
   ```sh
   nohup python main.py > Tarot_LLM_LineBot.log 2>&1 &
   ```

9. Activate Ngrok
   ```sh
   nohup ngrok http http://localhost:8080 > Tarot_LLM_LineBot_ngrok.log 2>&1 &
   ```
   
10. Get your API URL.
    ```sh
    wget http://127.0.0.1:4040/api/tunnels
    ```
    ```sh
    cat tunnels
    ```

    Find "public_url," which is your API URL.

11. Paste your URL into your Line Developer Webhook URL.
    ```sh
    [Your URL]/callback
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

* You can enter your question first, then press Shift+Enter to start a new line, and then input the tarot spread you want to use.

* The following tarot spreads are currently available:

1. Enter 1 or "抽一張牌": Draw one card.
2. Enter 2 or "時間之流": Draw time flow.
3. Enter 3 or "抽聖三角": Draw holy triangle.
4. Enter 4 or "抽六芒星": Draw hexagram.
5. Enter 5 or "抽無牌陣": Draw no spread.
6. Enter 6 or "抽關係排": Draw relationship spread.

* Or ask any questions you want to ask.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Chi Heng Ting - a0986772199@gmail.com

Project Link - https://github.com/Imding1211/Tarot_LLM_LineBot

<p align="right">(<a href="#readme-top">back to top</a>)</p>
