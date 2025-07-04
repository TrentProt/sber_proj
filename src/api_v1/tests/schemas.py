from typing import List, Union

from pydantic import BaseModel


class QAnswers(BaseModel):
    q_num: int
    answer_id: Union[int, None] = None


class StartFinishTestSchema(BaseModel):
    ok: bool
    test_was_passed: bool
    message: str


class AnswerSchema(BaseModel):
    id: int
    answer_text: str


class GetQuestionAndAnswersSchema(BaseModel):
    q_num: int
    question_text: str
    answers: List[AnswerSchema]
    tip: str


class UserAnswerSchema(BaseModel):
    id: Union[int, None]
    answer_text: Union[str, None]


class CorrectAnswerSchema(BaseModel):
    id: int
    correct_answer_text: str


class ResultAnswersUserSchema(BaseModel):
    q_num: int
    question_text: str
    user_answer: UserAnswerSchema
    is_correct: bool
    correct_answer: CorrectAnswerSchema


class ResultTestSchema(BaseModel):
    test_id: int
    count_correct_answer: int
    count_question: int
    score: int
    time_execution: int
    data_answers: List[ResultAnswersUserSchema]


class OkStatusSchema(BaseModel):
    ok: bool
    message: str


class CheckNewRewardSchema(OkStatusSchema):
    reward_id: Union[int, None]
