from pydantic import BaseModel, ValidationError, ConfigDict, EmailStr


class User(BaseModel):
    id: int
    name: str
    email: EmailStr | None = None

    # model_config = ConfigDict(strict=True)


if __name__ == '__main__':
    data = {
        'id': 32423423,
        'name': 'MDA',
        'email': '224@mail.db'
    }

    try:
        valid_data = User(**data)
        
        print(valid_data.model_dump())

    except Exception as ex:
        print(f'Error - {ex}')