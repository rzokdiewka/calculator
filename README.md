# Calculator

##  How to run
### Backend
Make sure you have `Python 3.9` or newer version installed.
> Recommended is to use virtual environment and create separate one for the project.

To install needed dependencies, from source folder `calculator/backend/` run 
```sh
pip install -r requirements.txt
``` 

Run project with 
```sh
uvicorn main:app --reload
```
>Swagger dokumentation of API http://127.0.0.1:8000/docs#/ should be available
### Frontend
>Recommended IDE Setup: [VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).  
>Customize configuration: See [Vite Configuration Reference](https://vitejs.dev/config/).

From source folder calculator/frontend/ run
```sh
npm install
```

Compile and Hot-Reload for Development

```sh
npm run dev
```
