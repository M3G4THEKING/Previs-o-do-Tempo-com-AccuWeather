# Previs-o-do-Tempo-com-AccuWeather

---

### Descrição do Repositório: Previsão do Tempo com AccuWeather

Este código é uma simples implementação em Python que utiliza a API do AccuWeather para obter informações meteorológicas de uma cidade especificada pelo usuário.

#### Funcionalidades:

1. **Busca de Chave de Localidade (Location Key):**
   A API do AccuWeather utiliza uma "chave de localidade" (ou `location key`) única para identificar cada cidade. O código contém uma função `obter_chave_localidade` que, dado o nome de uma cidade, consulta a API e retorna essa chave.

2. **Consulta de Clima Atual:**
   Uma vez que tenhamos a chave da localidade, podemos usar a função `obter_clima` para obter a previsão do tempo atual para essa cidade. A função recupera e exibe a temperatura em graus Celsius e uma breve descrição do clima (por exemplo, "Ensolarado", "Nublado").

#### Como Usar:

1. **Configuração:**
   - Certifique-se de ter o módulo `requests` instalado. Se não, instale-o usando `pip install requests`.
   - Defina sua chave de API do AccuWeather na variável `CHAVE_API`.

2. **Execução:**
   - Execute o script.
   - Quando solicitado, insira o nome da cidade para a qual deseja obter a previsão do tempo.
   - O script retornará a temperatura e a descrição do clima para a cidade inserida.

#### Dependências:

- Python 3.x
- Biblioteca `requests`

#### Considerações:

- A chave de API usada no código é apenas um exemplo. Para uso prolongado e consultas frequentes, é recomendável obter sua própria chave de API no site do AccuWeather.
- A API do AccuWeather pode ter limites de consultas diárias para chaves gratuitas.

---

Você pode usar essa descrição para criar um README profissional em seu repositório no GitHub. Recomendo também adicionar seções como "Como Contribuir" ou "Licença" se você estiver interessado em colaborações ou em especificar os direitos de uso do seu código.
