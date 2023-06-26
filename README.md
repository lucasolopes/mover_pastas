
# Mover Pastas

Acessar um determinado destino que contém várias pastas com diferentes arquivos dentro e identificar as pastas que possuem uma determinada extensão de arquivo. Em seguida, mover essas pastas para outro destino.

## Motivo:

Durante o trabalho, todos os tipos de pasta eram armazenados em uma única pasta e numerados. No entanto, ao filtrar para identificar as pastas específicas, como pasta X e pasta Y, não era possível distinguir qual pasta correspondia a qual. Para solucionar esse problema, um projeto foi criado para identificar as pastas com um formato de arquivo específico, no caso, pasta X, e movê-las para outro local. Dessa forma, o projeto facilitou a reorganização das pastas, garantindo uma melhor organização dos arquivos.



## Uso/Exemplos

```python
import mover_arquivos from 'mover'


mover_arquivos("origem", "destino","formato")

```

o formato deve ser escrito sem o "." Exemplo:
```python
    #Correto
    mover_arquivos("origem", "destino","formato")
    

    #Incorreto
    mover_arquivos("origem", "destino",".formato")
```




## Licença

[MIT](https://choosealicense.com/licenses/mit/)

