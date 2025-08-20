# Calculateur d'Année de Naissance

Une API FastAPI simple qui calcule l'année de naissance à partir de l'âge fourni.

## Fonctionnalités

- Calcul automatique de l'année de naissance basé sur l'âge actuel
- Validation des données d'entrée
- API RESTful avec documentation automatique
- Compatible avec Shopify Liquid

## Installation

1. Clonez ce repository
2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation locale

Lancez l'application :
```bash
python app.py
```

L'API sera disponible sur `http://localhost:8000`

## Endpoints

### POST /birthyear
Calcule l'année de naissance à partir de l'âge.

**Requête :**
```json
{
  "age": 25
}
```

**Réponse :**
```json
{
  "birth_year": 1998
}
```

### GET /
Page d'accueil avec informations sur l'API

### GET /health
Vérification de santé de l'API

### GET /docs
Documentation interactive de l'API (Swagger UI)

## Déploiement sur Render

1. Créez un nouveau service Web sur Render
2. Connectez votre repository GitHub
3. Configurez les paramètres :
   - **Build Command :** `pip install -r requirements.txt`
   - **Start Command :** `uvicorn app:app --host 0.0.0.0 --port $PORT`
4. Déployez !

## Intégration avec Shopify

Dans votre section Liquid Shopify, configurez l'URL de l'API :
```
https://votre-service.onrender.com/birthyear
```

## Exemple d'utilisation

```bash
curl -X POST "http://localhost:8000/birthyear" \
     -H "Content-Type: application/json" \
     -d '{"age": 30}'
```

Réponse :
```json
{
  "birth_year": 1993
}
```
# calculage
