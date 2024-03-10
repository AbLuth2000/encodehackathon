<a href="[[https://nuxt-ai-careguide.vercel.app]">
  <img alt="CareGuide Healthily" src="https://drive.google.com/file/d/1r9p1KJ-7wzZwcSEmT_j_GK8Lo_JP_6zp/view">
  <h1 align="center">CareGuide </h1>
</a>

<p align="center">
  An open-source AI chatbot app template built with Healthily API, OpenAI API, Perplexity, Whisper.
</p>
<br/>

## Summary
This project uses the Healthily API as the basis for diagnosing a patient's symptoms and outputting a report with the best service to go to for treatment.
The issue with the Healthily API is the 

## Features

- [Next.js](https://nextjs.org) App Router
- React Server Components (RSCs), Suspense, and Server Actions
- [Vercel AI SDK](https://sdk.vercel.ai/docs) for streaming chat UI
- Support for OpenAI (default), Anthropic, Cohere, Hugging Face, or custom AI chat models and/or LangChain
- [shadcn/ui](https://ui.shadcn.com)
  - Styling with [Tailwind CSS](https://tailwindcss.com)
  - [Radix UI](https://radix-ui.com) for headless component primitives
  - Icons from [Phosphor Icons](https://phosphoricons.com)
- Chat History, rate limiting, and session storage with [Vercel KV](https://vercel.com/storage/kv)
- [NextAuth.js](https://github.com/nextauthjs/next-auth) for authentication

## Model Providers

This template ships with OpenAI `gpt-3.5-turbo` as the default. However, thanks to the [Perplexity AI](https://perplexity.ai), you can switch LLM providers to [Anthropic](https://anthropic.com), [Cohere](https://cohere.com/), [Hugging Face](https://huggingface.co), or using [LangChain](https://js.langchain.com) And Whisper from OpenAI with just a few lines of code.


## Authors

This library is created by CareGuide and their team members, with contributions from:

- Ebhyuday Luthra
- Adrian Yan
- Emily Zhao
- Jetnor Muhaj
- Sonu Telkar
- Stefany Santos
