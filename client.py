"""
Self-Consistency Majority Voting and Semantic Answer Clusterer.
Zero external dependencies, standard library only.
"""

import re
from typing import Dict, List, Any, Optional

class SelfConsistencyVoterClient:
    """
    Implements Wang et al. Self-Consistency:
    Clusters multiple stochastic generation candidates, normalizes answers,
    and returns consensus majority vote with confidence margins.
    """

    def __init__(self):
        pass

    def normalize_answer(self, text: str) -> str:
        """Extracts final answer line or normalized tokens."""
        # Check for boxed or final answer keywords
        boxed = re.search(r"\\\\boxed{([^}]+)}", text)
        if boxed:
            return boxed.group(1).strip()

        final_ans = re.search(r"(?:the answer is|answer:)\s*([^\n\.]+)", text, re.IGNORECASE)
        if final_ans:
            return final_ans.group(1).strip()

        # Fallback to normalized last line
        lines = [l.strip() for l in text.strip().splitlines() if l.strip()]
        return lines[-1] if lines else text.strip()

    def vote(self, candidates: List[str]) -> Dict[str, Any]:
        """
        Groups candidates by normalized answer and determines majority vote.
        """
        if not candidates:
            return {"consensus_answer": None, "confidence": 0.0, "distribution": {}}

        vote_counts = {}
        candidate_mapping = {}

        for c in candidates:
            norm = self.normalize_answer(c)
            vote_counts[norm] = vote_counts.get(norm, 0) + 1
            if norm not in candidate_mapping:
                candidate_mapping[norm] = c

        sorted_votes = sorted(vote_counts.items(), key=lambda x: x[1], reverse=True)
        winner_norm, winner_votes = sorted_votes[0]
        confidence = round(winner_votes / len(candidates), 3)

        return {
            "consensus_answer": winner_norm,
            "representative_candidate": candidate_mapping[winner_norm],
            "confidence": confidence,
            "winner_votes": winner_votes,
            "total_candidates": len(candidates),
            "distribution": vote_counts
        }
