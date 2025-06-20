from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.tests import crud
from src.api_v1.tests.schemas import AddUserAttempt, GetQuestionAndAnswersSchema, \
    StartFinishTestSchema, ResultTestSchema
from src.core.dependencies import verify_access_token
from src.core.models import db_helper


router = APIRouter(tags=['Random tests'], prefix='/tests')


@router.get('/{test_id}/start')
async def generate_questions(
        test_id: int,
        token_payload: dict = Depends(verify_access_token),
        session: AsyncSession = Depends(db_helper.session_dependency)
) -> StartFinishTestSchema:
    user_id = token_payload.get('sub')
    return await crud.get_random_questions(
        test_id=test_id,
        user_id=user_id,
        session=session
    )


@router.get('/{test_id}/question/{q_num}')
async def get_question_answers(
        test_id: int,
        q_num: int,
        token_payload: dict = Depends(verify_access_token),
        session: AsyncSession = Depends(db_helper.session_dependency)
) -> GetQuestionAndAnswersSchema:
    user_id = token_payload.get('sub')
    return await crud.get_qa_for_test(
        q_num=q_num,
        test_id=test_id,
        user_id=user_id,
        session=session
    )


@router.post('{test_id}/finish')
async def add_results_test(
        test_id: int,
        data_answers: AddUserAttempt,
        token_payload: dict = Depends(verify_access_token),
        session: AsyncSession = Depends(db_helper.session_dependency)
) -> StartFinishTestSchema:
    user_id = int(token_payload.get('sub'))
    return await crud.finish_test(
        test_id=test_id,
        user_id=user_id,
        data_answers=data_answers,
        session=session
    )


@router.get('{test_id}/result')
async def get_result_test(
        test_id: int,
        token_payload: dict = Depends(verify_access_token),
        session: AsyncSession = Depends(db_helper.session_dependency)
) -> ResultTestSchema:
    user_id = int(token_payload.get('sub'))
    return await crud.get_result_test(
        test_id=test_id,
        user_id=user_id,
        session=session
    )
