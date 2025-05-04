import uvicorn
from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from typing import Annotated


# app.include_router(users.router)
# app.include_router(items.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {
        'q': q,
        'skip': skip,
        'limit': limit
    }

def query_3(q: str):
    print('QUERY_3 BEFORE YIELD')
    try:
        yield q
    except Exception:
        print('IN EXCEPT IN QUERY_3')

        raise HTTPException(status_code=500)

    print('QUERY_3 AFTER YIELD')


def query_2(q: str, query_3: Annotated[str, Depends(query_3)]):
    print('QUERY_2 BEFORE YIELD')
    try:
        yield q, query_3
    except Exception:
        print('IN EXCEPT IN QUERY_2')

        raise

    print('QUERY_2 AFTER YIELD')


def query_1(q: str, query_2: Annotated[str, Depends(query_2)]):
    print('QUERY_1 BEFORE YIELD')

    try:
        yield (q, query_2)
    except Exception:
        print('IN EXCEPT IN QUERY_1')

        raise
    print('QUERY_1 AFTER YIELD')


app = FastAPI(
    # dependencies=[
    #     Depends(query_1),
        # Depends(get_query_token)
    # ]
)


@app.get("/items/")
async def read_query(
        q: Annotated[str, Depends(query_1)]
):

    raise Exception('test')

    return {"q_s": q}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
