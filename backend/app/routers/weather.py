from fastapi import APIRouter
router = APIRouter(prefix='/weather')

@router.get('/current')
def current(city: str):
    return {}
