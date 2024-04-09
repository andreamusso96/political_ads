# LLama API setup

In order to set up the LLama API, you need to follow these steps.

### Step 1
Install docker (https://docs.docker.com/get-docker/)

### Step 2
Download the LLama model from Hugging Face [click here](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q2_K.gguf).

Note: This is the smallest model available. If you have more space you can download a bigger model from [this page](https://huggingface.co/TheBloke).
For example, you can download the [13B](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF) or [70B](https://huggingface.co/TheBloke/Llama-2-70B-Chat-GGUF) models. 
If you do this you will need to change the docker-compose.yml file to point to the correct file:
```    
      - MODEL=/var/model/llama-2-7b.Q4_K_M.gguf
```
Change ```llama-2-7b.Q4_K_M.gguf``` to the name of the model you downloaded (e.g., ```llama-2-13b.Q4_K_M.gguf``` for the 12B model).

Save the llama model in a folder on your computer. I call ```/path/to/llama/model``` the absolute path to the folder where the llama model is saved.

### Step 3
Change the docker-compose.yml file to point to the correct location for your llama model. Specifically, replace this line
```    volumes:
      - /Users/andrea/Desktop/PhD/Projects/Current/political_ads/llama_model:/var/model
  ```
with the ```/path/to/llama/model``` folder you saved the model in.

### Step 4
Open a terminal and navigate to the folder where the docker-compose.yml file is located. Then run the following command:
```docker-compose up```

### Step 5
You now have all the services running. 
You can access the llama.cpp api documentation going to http://localhost:5000/docs.

### Step 6
Run the example.py file to see if everything is working. The output should be:
```
EMBEDDING
[-0.00645211 -0.00773728  0.02126154 ...  0.00514225  0.01125308
 -0.01535881]
```