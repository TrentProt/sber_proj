from fastapi import APIRouter, Depends, UploadFile, File

from typing import List, Union

from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.topics import crud
from src.api_v1.topics.dependencies import get_id_user_or_none_from_cookie
from src.api_v1.topics.schemas import TopicsOut
from src.core.models import db_helper


router = APIRouter(tags=['Topics and Sections for main'])


@router.get('/topics')
@cache(expire=300)
async def get_topics(
        _: Union[str, None] = Depends(get_id_user_or_none_from_cookie),
        session: AsyncSession = Depends(db_helper.session_dependency)
) -> List[TopicsOut]:
    return await crud.get_topics(session=session)


@router.get('/sections_topics')
@cache(expire=300)
async def get_sections_topics(
        user_id: Union[str, None] = Depends(get_id_user_or_none_from_cookie),
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_sections_topics_crud(user_id=user_id, session=session)


@router.get('/section/{section_topic_id}')
async def tests_case_in_section(
        section_topic_id: int,
        user_id: Union[str, None] = Depends(get_id_user_or_none_from_cookie),
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_section_and_tests(
        user_id=user_id,
        section_topic_id=section_topic_id,
        session=session
    )


@router.post('/section/upload_image/{section_topic_id}')
async def upload_image_section(
        section_topic_id: int,
        file: UploadFile = File(...),
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.upload_image_section_topic(
        section_topic_id=section_topic_id,
        file=file,
        session=session
    )