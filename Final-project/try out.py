request_path = 'http://localhost:8080/geneList?chromosome=gg&start=6&end=8'
print(request_path.split('=')[1].split('&')[0])
print(request_path.split('=')[2].split('&')[0])
print(request_path.split('=')[-1])


