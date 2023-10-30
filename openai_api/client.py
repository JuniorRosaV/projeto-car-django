import openai

def auto_biography(model,brand,year):

    prompt = '''Me de a descrição para venda do carro {}{}{},
    qual a media de combustivel gasto por km e descreva o motor do carro, em 250 caracteres'''
   
    openai.api_key = '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'
    prompt = prompt.format(brand,model,year)
    response = openai.Completion.create(
            model = 'text-davinci-003',
            prompt = prompt,
            max_tokens = 1000,
    )
        
    return response ['choices'][0]['text']