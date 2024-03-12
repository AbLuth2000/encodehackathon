<a href="[[https://nuxt-ai-careguide.vercel.app]">
  <img alt="CareGuide Healthily" src="https://github.com/AbLuth2000/encodehackathon/blob/main/public/Computer%20User%20Interface.png">
  <h1 align="center">CareGuide </h1>
</a>

<p align="center">
  An open-source AI chatbot app template built with Healthily API, OpenAI API, Perplexity, Whisper.
</p>
<br/>

## Summary
This project uses the Healthily API as the basis for diagnosing a patient's symptoms and outputting a report with the best service to go to for treatment.
Issues that were noticed with the Healthily API werer that after receiving advice on the Healthily DOT, seeing a doctor is not needed. However, users still decide to book a GP appointment as they do not fully trust the outcome of the diagnosis. This is a practical issue about trust - the platform is not serving its true purpose of deferring mild patients away from GPs, which both increases the workload on GPs and also doctors, where it is unnecassary.

We are proposing a compassion-focused and decision-oriented chatbot that empowers users to make informed healthcare decisions with trust and confidence. This solution uses the Healthily API as the base to diagnose and run an example consultation workflow. This process was both slow and clunky due to the survey-like nature of the current consultation workflow. Our solution is more personable with enhanced outputs using external LLMs to make the outputs more comforting and compassionate. However, this in no way impacts the outputs that Healthily's API provides and all required information is consistent which required payloads. Our external LLMs do no triaging and are simply used for language processing and improving. We also allow for more accessibility focused on targeting groups such as elderly people, people with neurological impairments and people with disabilities who may have trouble using the current Healthily workflow. We offer a text-to-speech feature for our outputs using OpenAI's Whisper API which allows these target groups to have greater accessibility to the platform. 

## Technology Stack
Our intention with this solution was the following workflow:
- A react front-end acting as a chatbot - very similar to a WhatsApp coversation.
- This takes both the user inputs and passes them through a Flask API into our backend python functions.
- Our python functions we call the Healthily API with their inputs.
- We then use the Healthily API's outputs and pass them into our 'enhance' function which uses Perplexity's API and makes the outputs more compassionate. These new and improved outputs are then returned to the react app as a message. The original meaning of Healthily's outputs remains the same, as do the sentences themselves. This means nothing is lst within the consultation workflow.


## Model Providers

This template ships with OpenAI `gpt-3.5-turbo` as the default. However, thanks to the [Perplexity AI](https://perplexity.ai), you can switch LLM providers to [Anthropic](https://anthropic.com), [Cohere](https://cohere.com/), [Hugging Face](https://huggingface.co), or using [LangChain](https://js.langchain.com) And Whisper from OpenAI with just a few lines of code.


## Authors

This library is created by CareGuide and their team members, with contributions from:

- Abhyuday Luthra
- Adrian Yan
- Emily Zhao
- Jetnor Muhaj
- Srivatsa Telkar
- Stefany Santos
