utilisateurs = [
    {"nom": "Alice", "age": 25},
    {"nom": "Bob", "age": 17},
    {"nom": "Charlie", "age": 19},
    {"nom": "David", "age": 15}
]

majeurs = [u.get('nom') for u in utilisateurs if u.get('age', 0) >= 18]
print(majeurs)
