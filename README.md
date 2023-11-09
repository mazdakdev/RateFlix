# RateFlix - A safehome for Movie buffs
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
![GitHub](https://img.shields.io/github/license/mazdakdev/RateFlix)
![GitHub stars](https://img.shields.io/github/stars/mazdakdev/RateFlix)
![GitHub watchers](https://img.shields.io/github/watchers/mazdakdev/RateFlix)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/t/mazdakdev/RateFlix)

<img width="1440" alt="Screenshot 2023-11-09 at 6 19 03 PM-min" src="https://github.com/mazdakdev/RateFlix/assets/60855141/7a4bf55a-c5a4-4366-a1b8-aa7dfef50132">

This full stack application allows users to browse movies, write reviews, and receive personalized recommendations. It utilizes Neural Collaborative Filtering (NCF) for recommendations and LSTM neural networks for sentiment analysis of the provided comment in the scale of 0 to 5.

## Architecture
TODO

## Team and Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://jakebolam.com"><img src="https://avatars.githubusercontent.com/u/3534236?v=4?s=100" width="100px;" alt="Jake Bolam"/><br /><sub><b>Jake Bolam</b></sub></a><br /><a href="#infra-jakebolam" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/mazdakdev/RateFlix/commits?author=jakebolam" title="Tests">⚠️</a> <a href="https://github.com/mazdakdev/RateFlix/commits?author=jakebolam" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## Technologies
**The Recommender System / Sentiment Analysis:**
- Python - High-level Progeamming Language
- Pandas - Python Data Analysis Library
- Numpy  - Python High-level Mathematical Functions
- NTLK   - Python Natural Language Toolkit
- scikit-learn - Python Machine Learning Library
- Pytorch - Python Neural Networks and Deep Learning Library

**Datasets**
TODO

**Frontend:**
- Vue3 - The Progressive JavaScript Framework
- Nuxt3 - The Intuitive Vue Framework · Nuxt
- Pinia - State Management Framework For Vue.js.
- Tailwind.css - Open Source CSS Framework
- [OMDb API](https://www.omdbapi.com/)
- HTML/CSS

**Backend:** 
- Python - High-level Programming Language
- Django -  High-level Python web framework
- DRF - Django REST framework
- JWT Auth and ...

## Development

### Clone The Repo
  ```bash
  user@host:~/$ git clone https://github.com/mazdakdev/RateFlix && cd Rateflix
  ```

### Create `.env` file in `core/`
   ```
    SECRET_KEY=your-django-secret-key
    DEBUG=True
    CORS_ALLOW_ALL_ORIGINS=True
   ```
   
   Note: you can get Django secret key from [here](https://djecrety.ir/).
   
### Start Backend Development Server
   ```bash
   user@host:~/$ cd core && poetry install && poetry run python manage.py runserver
   ```

### Start Fronted Development Server
  ```bash
  user@host:~/$ cd rate-flix && npm install && npm run dev
  ```

## Deployment


  ### Getting Started with Docker
  TODO
  1. Clone repo


## Deploy manualy


## Contribution
All type of contributions are welcommed.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!