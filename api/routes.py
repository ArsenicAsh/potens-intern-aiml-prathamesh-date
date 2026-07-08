from fastapi import APIRouter
from pydantic import BaseModel

from services.generator import generate_answer
from services.contradict import check_contradiction

router = APIRouter()


class AskRequest(BaseModel):
    question: str


class ContradictRequest(BaseModel):
    document1: str
    document2: str
    topic: str


@router.post("/ask")
def ask(request: AskRequest):

    return generate_answer(request.question)


@router.post("/contradict")
def contradict(request: ContradictRequest):

    return check_contradiction(
        request.document1,
        request.document2,
        request.topic
    )