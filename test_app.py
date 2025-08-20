import requests
import json
from datetime import datetime

def test_birth_year_calculator():
    """Test de l'API de calcul d'année de naissance"""
    
    # URL de l'API (modifiez selon votre déploiement)
    base_url = "http://localhost:8000"
    
    print("🧪 Test du calculateur d'année de naissance")
    print("=" * 50)
    
    # Test 1: Calcul normal
    print("\n1. Test avec un âge valide (25 ans)")
    try:
        response = requests.post(
            f"{base_url}/birthyear",
            json={"age": 25},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            current_year = datetime.now().year
            expected_year = current_year - 25
            print(f"✅ Succès! Année de naissance calculée: {result['birth_year']}")
            print(f"   Âge fourni: 25 ans")
            print(f"   Année attendue: {expected_year}")
        else:
            print(f"❌ Erreur: {response.status_code} - {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Impossible de se connecter à l'API. Assurez-vous qu'elle est en cours d'exécution.")
        return
    
    # Test 2: Âge négatif
    print("\n2. Test avec un âge négatif")
    try:
        response = requests.post(
            f"{base_url}/birthyear",
            json={"age": -5},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 400:
            print("✅ Succès! Erreur correctement gérée pour un âge négatif")
        else:
            print(f"❌ Erreur: L'API devrait rejeter un âge négatif")
            
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
    
    # Test 3: Âge trop élevé
    print("\n3. Test avec un âge invalide (200 ans)")
    try:
        response = requests.post(
            f"{base_url}/birthyear",
            json={"age": 200},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 400:
            print("✅ Succès! Erreur correctement gérée pour un âge invalide")
        else:
            print(f"❌ Erreur: L'API devrait rejeter un âge de 200 ans")
            
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
    
    # Test 4: Endpoint de santé
    print("\n4. Test de l'endpoint de santé")
    try:
        response = requests.get(f"{base_url}/health")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Succès! API en bonne santé: {result}")
        else:
            print(f"❌ Erreur: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Tests terminés!")

if __name__ == "__main__":
    test_birth_year_calculator()
