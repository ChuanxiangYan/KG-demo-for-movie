from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:3030/kg_demo_movie/query")
sparql.setQuery("""
    PREFIX : <http://www.kgdemo.com#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT ?n WHERE {
      ?s rdf:type :Person.
      ?s :personEnglishName 'Gong Li'.
      ?s :hasActedIn ?o.
      ?o :movieTitle ?n.
      ?o :movieRating ?r.
    FILTER (?r >= 7)
    }
""")
sparql.setReturnFormat(JSON)
a = sparql.query()
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["n"]["value"])