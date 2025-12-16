# 🚀 Démarrage Rapide - Colab AI Coder

**Assitant IA complet basé sur Qwen-2.5-Coder 7B + VS Code**

---

## ⚡ Démarrage en 5 minutes (Google Colab)

### 1️⃣ Ouvrir le notebook

1. Allez à [Google Colab](https://colab.research.google.com/)
2. Cliquez **Fichier** → **Ouvrir un notebook**
3. Sélectionnez **GitHub**
4. Cherchez : `yourusername/colab-ai-coder`
5. Ouvrez `notebooks/qwen-assistant.ipynb`

### 2️⃣ Exécuter les cellules dans l'ordre

1. **Vérifier l'environnement** (GPU/RAM)
2. **Installer les dépendances** (~2 minutes)
3. **Charger le modèle** (~3 minutes)
4. **Tester l'inférence** (quick test)
5. **Démarrer l'API** (FastAPI server)

### 3️⃣ Récupérer l'URL publique

Après la cellule 7, vous aurez une URL publique :
```
https://xxxx-xxxx-ngrok-io
```

Utilisez cette URL pour connecter VS Code.

---

## 🖥️ Démarrage Local (Dev)

### Windows
```powershell
.\\setup-dev.ps1
```

### Linux/Mac
```bash
bash setup-dev.sh
```

### Ou avec Make
```bash
make dev
make run
```

L'API sera disponible sur `http://localhost:8000`

---

## 🐳 Démarrage avec Docker

```bash
docker-compose up
```

Services lancés :
- API FastAPI: http://localhost:8000
- Redis cache: localhost:6379
- Jupyter: http://localhost:8888

---

## 📝 Exemples d'utilisation

### Générer du code

**cURL:**
```bash
curl -X POST http://localhost:8000/api/v1/assistant/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "def fibonacci(n):",
    "task": "generate",
    "max_tokens": 150
  }'
```

**Python:**
```python
import requests

response = requests.post(
    "http://localhost:8000/api/v1/assistant/generate",
    json={
        "prompt": "def fibonacci(n):",
        "task": "generate",
        "max_tokens": 150
    }
)

print(response.json()["response"])
```

### Refactorer du code

```bash
curl -X POST http://localhost:8000/api/v1/assistant/refactor \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "for i in range(len(list)): print(i)",
    "task": "refactor"
  }'
```

### Auditer la sécurité

```bash
curl -X POST http://localhost:8000/api/v1/assistant/audit \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "import os; os.system(input())",
    "task": "audit"
  }'
```

---

## 📚 Documentation

| Document | Description |
|----------|------------|
| [docs/colab-setup.md](docs/colab-setup.md) | Guide complet Colab |
| [docs/api.md](docs/api.md) | Référence API |
| [README.md](README.md) | Vue d'ensemble |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Guide contribution |
| [ROADMAP.md](ROADMAP.md) | 90+ features futures |

---

## 🔌 Connecter VS Code

### Extension Colab AI Coder (Coming Soon)

1. Ouvrez VS Code
2. Extensions (Ctrl+Shift+X)
3. Cherchez "Colab AI Coder"
4. Installez

### Configuration

1. Ouvrez Command Palette (Ctrl+Shift+P)
2. "Colab AI Coder: Configure API"
3. Collez l'URL de Colab
4. Done!

### Utilisation

Clic-droit sur le code :
- **Generate** : Générer du code
- **Refactor** : Refactorer
- **Debug** : Déboguer
- **Audit** : Audit sécurité

---

## 🧪 Tests

```bash
# Exécuter tous les tests
cd backend
pytest tests/ -v

# Avec couverture
pytest tests/ --cov=src --cov-report=html

# Test spécifique
pytest tests/test_health.py -v
```

---

## 🔧 Commandes utiles

```bash
# Linter
make lint

# Formatter
make format

# Type check
make type-check

# Security scan
make security

# Nettoyer
make clean

# Docker build
make docker-build

# Docker run
make docker-run
```

---

## 📊 Ressources utilisées

**Colab Free:**
- RAM: 12GB (disponible: ~10GB)
- GPU: T4 (7-8GB VRAM)
- Modèle: Qwen-2.5-Coder 7B Q4_K_M (5.2GB)
- **Total**: ~6.7GB ✅ Ça rentre!

**Local:**
- GPU: Recommandé (6GB+ VRAM)
- CPU: Fallback automatique si OOM
- RAM: 8GB minimum

---

## ❓ Troubleshooting

### Out of Memory (OOM)

```python
# Colab: Runtime → Restart runtime

# Local: Réduire max_tokens ou utiliser modèle 1.5B
```

### Connexion ngrok échouée

```python
# Installer pyngrok
pip install pyngrok
```

### API lente

```python
# Augmenter num_gpu_layers
# Réduire contexte (num_ctx)
# Passer au modèle 1.5B
```

---

## 📦 Structure de dépôt

```
colab-ai-coder/
├── notebooks/          # Colab setup
├── backend/            # API FastAPI
├── docs/               # Documentation
├── .github/workflows/  # CI/CD
└── Dockerfile          # Container
```

---

## 🔒 Sécurité

- ✅ Snyk code scan
- ✅ Container scanning
- ✅ Pre-commit hooks
- ✅ Docker non-root
- ✅ .env secrets
- ✅ Type checking strict

---

## 📞 Support

- 📖 Docs: [docs/](docs/)
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions
- 📧 Email: support@example.com

---

## 📄 License

MIT License - Voir [LICENSE](LICENSE)

---

**Prêt? Allez à [Colab](https://colab.research.google.com/) et ouvrez le notebook!** 🎉

Pour plus d'infos: [README.md](README.md)
