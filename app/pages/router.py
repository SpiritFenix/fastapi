from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='templates')


@router.get('/test')
async def get_students_html(request: Request):
    return templates.TemplateResponse(name='test.html', context={'request': request})
