# 🚀 Colab AI Coder

**Assistant IA complet pour le développement** basé sur Qwen-2.5-Coder 7B, intégré à VS Code et Google Colab.

## ✨ Fonctionnalités MVP (Phase 1)

- ✅ **Assistant de code** : génération, complétion, refactorisation
- ✅ **Refactorisation automatique** : extraction, renommage, optimisation
- ✅ **Debug assistant** : diagnostic et suggestions de fix
- ✅ **Audit sécurité** : Snyk, semgrep, bandit intégrés
- ✅ **Pre-commit hooks** : ruff, black, isort automatiques
- ✅ **Tests automatisés** : pytest avec couverture
- ✅ **CI/CD GitHub Actions** : lint, test, scan sécurité
- ✅ **Docker hardening** : non-root, image optimisée
- ✅ **Cache et historique** : réutilisation des prompts
- ✅ **Templates de prompts** : spécialisés par tâche
- ✅ **Type checking** : pyright/mypy strict
- ✅ **Gestion des secrets** : .env.example, validation
- ✅ **Observabilité** : logs, erreurs, monitoring
- ✅ **Documentation interactive** : README + guide Colab
- ✅ **Release automation** : changelog, image Docker

## 📋 90+ Fonctionnalités futures (Phase 2+)

À venir...

## 🏗️ Architecture

```
colab-ai-coder/
├── notebooks/                 # Notebooks Colab (Qwen-2.5-Coder)
│   └── qwen-assistant.ipynb  # Setup Colab + modèle
├── backend/                   # API FastAPI + modèle IA
│   ├── src/
│   │   ├── main.py           # Point d'entrée FastAPI
│   │   ├── config.py         # Configuration
│   │   ├── models/           # Logique modèle
│   │   └── api/              # Routes API
│   └── tests/                # Tests pytest
├── vscode-extension/         # Extension VS Code
├── .github/workflows/        # CI/CD GitHub Actions
├── docs/                     # Documentation
└── docker-compose.yml        # Stack locale
```

## 🚀 Démarrage rapide

### Option 1 : Google Colab (Gratuit)
1. Ouvrir le notebook `notebooks/qwen-assistant.ipynb`
2. Sélectionner kernel **Colab**
3. Exécuter les cellules d'installation
4. Lancer l'API FastAPI

### Option 2 : Local + Docker
```bash
docker-compose up -d
```

### Option 3 : VS Code Extension
1. Installer l'extension depuis Marketplace
2. Connecter au backend (local ou Colab)
3. Utiliser l'assistant directement dans VS Code

## ⚙️ Configuration Colab (Qwen-2.5-Coder 7B)

**Paramètres d'optimisation :**
- Quantification : `Q4_K_M` (7B → ~5.2GB VRAM)
- Contexte : `num_ctx=4096` (max GPU free)
- Température : `0.2` (génération déterministe)
- Top-p : `0.9`, Top-k : `40`
- Offload dynamique : CPU/GPU split si OOM

**Estimation VRAM :**
- RAM Colab Free : 12 GB
- VRAM GPU : ~7-8 GB
- Modèle Q4 : ~5.2 GB
- Overhead : ~1.5 GB
- **Total** : ~7.7 GB (OK ✅)

## 🔒 Sécurité

- ✅ Snyk code scan + container scan
- ✅ Semgrep + bandit pour les secrets
- ✅ Pre-commit hooks obligatoires
- ✅ Docker non-root
- ✅ Type checking strict (pyright)
- ✅ GitHub Actions CI/CD sécurisée

## 📖 Documentation

- [Guide Colab](docs/colab-setup.md)
- [API REST](docs/api.md)
- [VS Code Extension](docs/vscode-extension.md)
- [Architecture](docs/architecture.md)
- [Roadmap](docs/roadmap.md)

## 📞 Support

- Issues : GitHub Issues
- Discussions : GitHub Discussions
- Docs : [docs/](docs/)

---

**Made with ❤️ for developers** — 2025
