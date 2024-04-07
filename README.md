# Calculator

A web-based calculator application that performs basic arithmetic operations. The focus is on a robust design that
separates business logic from presentation, and is extendable for future enhancements. In the future, it required to add
tests. It still needs better documentation e.g. docstrings.

## Functionality

1. Core Operations: the calculator support addition (+), subtraction (-), division (/), and multiplication (*).
2. Client-side Input Format: it takes an operator and two operands as inputs.
3. REST API Integration: All operations and their results are accessible via a REST API.
4. Server-Side Logic: The business logic, including calculations and result processing - implemented on the server side.
5. Client-Side Presentation: The client-side application handles only the presentation aspects and interacts with the
   server using REST API.
6. Multi-Application Support: The REST API accommodate multiple client applications without requiring changes to the API
   contract.

As an extension, for more complex expression, function `make_complex_calculation()` in `feature.py` script was
developed. It contains implementation to perform arithmetic operations in correct order (indirectly organize the
operators and operands in a specific order). It is just prototype, taking as an arguments data in the same format as
received from app API.

## How to run

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

> Swagger dokumentation of API http://127.0.0.1:8000/docs#/ should be available

### Frontend

> Recommended IDE
>
Setup: [VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (
> and disable Vetur).  
> Customize configuration: See [Vite Configuration Reference](https://vitejs.dev/config/).

From source folder calculator/frontend/ run

```sh
npm install
```

Compile and Hot-Reload for Development

```sh
npm run dev
```
