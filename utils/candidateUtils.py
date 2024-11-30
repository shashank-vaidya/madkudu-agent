from typing import List
from custom_types.custom_types import Candidate, ScoredCandidate, CandidateScore

def combine_candidates_with_scores(
    candidates: List[Candidate], candidate_scores: List[CandidateScore]
) -> List[ScoredCandidate]:
    score_dict = {score.id: score for score in candidate_scores}
    scored_candidates = []
    for candidate in candidates:
        score = score_dict.get(candidate.id)
        if score:
            scored_candidates.append(
                ScoredCandidate(
                    id=candidate.id,
                    name=candidate.name,
                    email=candidate.email,
                    bio=candidate.bio,
                    skills=candidate.skills,
                    score=score.score,
                    reason=score.reason,
                )
            )
    return scored_candidates
