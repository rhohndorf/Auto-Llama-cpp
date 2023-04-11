# Auto-Llama-cpp: An Autonomous Llama Experiment
This is a fork of April 11th of Auto-GPT. I hacked the llama.cpp support in an hour without knowing much about how Auto-GPT actually works (yay for AI safety ;-)). 
So this is more of a proof of concept. I tried it with the vicuna-13B-4bit model. It's sloooow and most of the time you're fighting with the too small context window size, but sometimes it works and it's really quite astonishing what even such a small model comes up with. But obviously don't expect GPT-4 brilliance here.
Running the model with gptq on the GPU  might make the latency a little more bearable. I'll add a better README soon. When in doubt how to do something look in the Auto-GPT repo.
