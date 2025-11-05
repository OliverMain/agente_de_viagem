from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from pydantic import Field, BaseModel
from dotenv import load_dotenv
from langchain_core.globals import set_debug
import os

set_debug(True)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class Destino(BaseModel):
    cidade:str = Field("A cidade recomendada para visitar")
    motivo:str = Field("motivo pelo qual é interessante visitar a cidade")

class Restaurantes(BaseModel):
    cidade:str = Field("A cidade recomendada para visitar")
    restaurantes:list[str] = Field("Os restaurantes recomendados para visitar")

class AtividadesCulturais(BaseModel):
    cidade:str = Field("A cidade recomendada para visitar")
    atividades:list[str] = Field("As atividades culturais recomendadas para visitar")

parser = JsonOutputParser(pydantic_object=Destino)
parser_restaurantes = JsonOutputParser(pydantic_object=Restaurantes)
parser_cultural = JsonOutputParser(pydantic_object=AtividadesCulturais)

prompt_cidade = ChatPromptTemplate.from_template(
    """
    Sugira uma cidade dado o meu interesse por {interesse}
    {formato_saida}
    """,
    partial_variables={"formato_saida": parser.get_format_instructions()}   
)

prompt_restaurantes = ChatPromptTemplate.from_template(
    """
    Sugira restaurantes dado o meu interesse por {interesse}
    Dado a cidade {cidade}
    {formato_saida}
    """,
    partial_variables={"formato_saida": parser_restaurantes.get_format_instructions()}   
)

promtp_cultural = PromptTemplate.from_template(
    """
    Sugira atividades culturais dado o meu interesse por {interesse}
    Dado a cidade {cidade}
    {formato_saida}
    """,
    partial_variables={"formato_saida": parser_cultural.get_format_instructions()}   
)   

modelo = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key=api_key
)

cadeia_1 = prompt_cidade | modelo | parser
cadeia_2 = prompt_restaurantes | modelo | parser_restaurantes
cadeia_3 = promtp_cultural | modelo | parser_cultural

cadeia = (cadeia_1 | cadeia_2 | cadeia_3)


resposta = cadeia_1.invoke(
    {
        "interesse" : "praias"
    }
)
print(resposta)