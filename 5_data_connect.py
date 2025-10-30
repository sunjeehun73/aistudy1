from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='sample.csv')
data = loader.load()
print(data)