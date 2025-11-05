# 🧭 Agente de Viagem  
**Um agente de viagem inteligente construído em Python, utilizando LangChain, LangGraph e a metodologia RAG.**

---

## 📘 Visão Geral  
Este projeto tem como objetivo desenvolver um **agente de viagem baseado em IA** que possa compreender consultas de usuários, consultar bases de dados/contextos (“retrieval”), e gerar respostas relevantes (via “generation”) para ajudar no **planejamento de viagens**.

A arquitetura incorpora:
- 🐍 **Python** como linguagem principal  
- 🧩 **LangChain** para orquestração de LLMs, prompts e cadeias (chains)  
- 🔗 **LangGraph** para modelagem de fluxos e grafos lógicos  
- 📚 **RAG (Retrieval-Augmented Generation)** para combinar fontes de conhecimento com geração de resposta  

---

## ✨ Funcionalidades Principais  
- 💬 Interaja com o agente para planejar viagens, buscar hospedagens e explorar destinos  
- 🔍 Recupera informações de documentos, APIs ou bases de dados integradas  
- 🧠 Gera respostas contextualizadas e recomendações personalizadas  
- ⚙️ Estrutura modular — fácil de adaptar a novas fontes de dados ou modelos de linguagem  

---

## 🏗️ Arquitetura  

1. **Fonte de Dados / Retrieval**  
   Conjunto de documentos, APIs ou bases estruturadas com informações sobre destinos, hospedagens, transportes e atividades.  

2. **Camada LangChain**  
   Montagem de *chains*, prompts e lógica que conectam a consulta → recuperação → geração de resposta.  

3. **Camada LangGraph**  
   Modelagem visual e lógica dos fluxos internos entre os módulos.  

4. **Modelo de Geração (LLM)**  
   Responsável por produzir as respostas com base nas informações recuperadas e contexto.  

5. **Interface (CLI / UI / Bot)**  
   Permite interação direta com o agente.  

---

## ⚙️ Instalação  

```bash
git clone https://github.com/OliverMain/agente_de_viagem.git
cd agente_de_viagem
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
pip install -r requirements.txt
