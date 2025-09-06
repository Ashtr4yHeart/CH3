import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/"

					
def mostrar_menu():				
	print("\n--- PokeAPI Demo ---")				
	print("1. Obtener información de un Pokémon (GET)")				
	print("2. Listar tipos de Pokémon (GET con parámetros)")				
	print("3. Simular búsqueda (404 Not Found)")				
	print("4. Salir")				
	return input("Selecciona una opción: ").strip()				
					
def demo_get():				
	"Demostración de GET - Obtener recurso"				
	nombre = input("Ingresa el nombre de un Pokémon: ").strip().lower()				
	if not nombre:				
	   print("❌ No ingresaste ningún nombre.")				
	   return				
			 		
	url = f"{BASE_URL}pokemon/{nombre}"				
	print(f"\n🔎 Realizando GET a: {url}")				
	response = requests.get(url)				
					
	if response.status_code == 200:				
	    data = response.json()				
	    print("\n✅ ¡Pokémon encontrado!")				
	    print(f"Nombre: {data['name'].capitalize()}")				
	    print(f"Altura: {data['height'] / 10} m")				
	    print(f"Peso: {data['weight'] / 10} kg")				
	    print("Tipos:")				
	    for tipo in data['types']:				
	        print(f"- {tipo['type']['name'].capitalize()}")				
					
	    print("\n📦 Resumen del JSON:")				
	    resumen = {k: data[k] for k in ['id', 'name', 'height', 'weight']}				
	    print(json.dumps(resumen, indent=2))				
	else:				
	    print(f"\n❌ Error {response.status_code}: Pokémon no encontrado.")				
					
def demo_get_params():				
	"Demostración de GET con parámetros"				
	limit = input("¿Cuántos tipos de Pokémon quieres listar? (default 20): ").strip()				
	if not limit.isdigit():				
	   print("❌ Ingresa un número válido.")				
	   return				
					
	url = f"{BASE_URL}type?limit={limit}"				
	print(f"\n🔎 Realizando GET a: {url}")				
	response = requests.get(url)				
					
	if response.status_code == 200:				
	    data = response.json()				
	    print(f"\n✅ Lista de tipos de Pokémon (mostrando hasta {limit}):")				
	    for tipo in data['results']:				
	        print(f"- {tipo['name'].capitalize()}")				
					
	    print("\n📄 Headers relevantes de la respuesta:")				
	    for header in ['content-type', 'date', 'cache-control']:				
	         print(f"{header}: {response.headers.get(header)}")				
	else:				
	    print(f"\n❌ Error {response.status_code}: No se pudo obtener la lista.")				
					
def demo_not_found():				
	"Demostración de error 404"				
	nombre = "este_pokemon_no_existe"				
	url = f"{BASE_URL}pokemon/{nombre}"				
					
	print(f"\n🔎 Realizando GET a: {url} (simulando error)")				
	response = requests.get(url)				
					
	print(f"\n❌ Código de estado: {response.status_code}")				
	print("Mensaje: El recurso solicitado no existe.")				
	print("👉 Esto ocurre cuando se consulta un endpoint incorrecto.")

def main():
	print("""
	====================
	     DEMO DE API CON POKEAPI   
	====================
	   Interactuemos con https://pokeapi.co/
	   para aprender conceptos de APIs:
	   
	   * Método HTTP GET
	   * Parametros de consulta 
	   * Códigos de estado (200, 404)
	   Respuestas en formato JSON
	   Headres de la respuesta
    """)
	while True:
		opcion = mostrar_menu()
		if opcion == "1":
			demo_get()
		elif opcion == "2":
			 demo_get_params()
		elif opcion == "3":
			 demo_not_found()
		elif opcion == "4":
			print("¡Hasta luego!")
			break
		else:
			print("Opción no valida. Intenta de nuevo")

if __name__ == "__main__":
   main()


