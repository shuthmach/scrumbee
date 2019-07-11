### Function that uses Google Natural Language API's entity analysis function to return entity types for a list of entity names contained
### in a DataFrame index. This allows entity analysis functionality to be used on multiple entries across a DataFrame rather than 
### discrete chunks of text.

def find_entities(df):
    ### This function takes a DataFrame with an index containing entity names, and uses natural language search to 
    ### identify types of entities. The output is a DataFrame containing the entity names and numeric types.
    
    # Instantiates a client
    client = language.LanguageServiceClient()

    name_types = pd.DataFrame(columns = ['Name', 'Type'])
    name_types['Name'] = df.index

    # Detects the entities in the text
    for i in range(len(name_types)):
        text = name_types.iloc[i,0]
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)
        try:
            entity = client.analyze_entities(document=document)
        except:
            pass
        try:
            name_types['Type'][i] = entity.entities[0].type
        except:
            pass
    return name_types
