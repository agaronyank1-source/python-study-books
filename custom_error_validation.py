from typing import Any
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def extract_field(loc: tuple[Any, ...]) -> str:
    parts = list(loc)
    if parts and parts[0] in {"body", "query", "path", "header"}:
        return parts[1:]
    return ".".join(str(p) for p in parts) if parts else "unknown"


def register_handlers(app) -> None:

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        errors = []
        for err in exc.errors():
            errors.append({"loc": extract_field(err["loc"]), "msg": err["msg"], "type": err["type"]})
        return JSONResponse(
            status_code=422,
            content={"detail": "Ошибка валидации", "Ошибки": errors},
        )

# TODO: сделать и на все остальные ошибки
