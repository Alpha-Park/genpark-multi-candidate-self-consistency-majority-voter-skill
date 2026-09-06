"""
Demonstration of genpark-multi-candidate-self-consistency-majority-voter-skill
"""

from client import SelfConsistencyVoterClient

def main():
    voter = SelfConsistencyVoterClient()

    # 5 sampled reasoning responses to math problem
    samples = [
        "Let x be the speed. x + 5 = 20 => The answer is 15",
        "Step 1: calculate drift. Result: 15 km/h. Answer: 15",
        "Maybe the value is 12 due to friction.",
        "Solving the system yields \\boxed{15}",
        "The answer is 15"
    ]

    result = voter.vote(samples)
    print("=== SELF-CONSISTENCY MAJORITY VOTE ===")
    print("Consensus Answer:", result["consensus_answer"])
    print(f"Confidence: {result['confidence'] * 100}% ({result['winner_votes']}/{result['total_candidates']} votes)")
    print("Vote Distribution:", result["distribution"])

if __name__ == "__main__":
    main()
