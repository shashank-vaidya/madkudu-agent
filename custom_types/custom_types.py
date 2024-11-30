from pydantic import BaseModel

class Candidate(BaseModel):
    id: str
    name: str
    email: str
    bio: str
    skills: str

class CandidateScore(BaseModel):
    id: str
    score: int
    reason: str


class ScoredCandidate(BaseModel):
    id: str
    name: str
    email: str
    bio: str
    skills: str
    score: int
    reason: str
