import datetime

class CryptidReport:
    """Represents a single report about a cryptid sighting."""
    def __init__(self, cryptid_name: str, location: str, description: str, 
                 image_clarity_score: int, num_witnesses: int, reporter_name: str = "Anonymous"):
        self.cryptid_name = cryptid_name
        self.location = location
        self.description = description
        self.image_clarity_score = image_clarity_score # 0-10, 10 being perfectly clear
        self.num_witnesses = num_witnesses
        self.reporter_name = reporter_name
        self.report_date = datetime.date.today()

    def __str__(self):
        return (
            f"Report for {self.cryptid_name} by {self.reporter_name} on {self.report_date}:\n"
            f"  Location: {self.location}\n"
            f"  Description: {self.description[:70]}{'...' if len(self.description) > 70 else ''}\n"
            f"  Image Clarity: {self.image_clarity_score}/10\n"
            f"  Witnesses: {self.num_witnesses}"
        )

class ReportQualityEvaluator:
    """Evaluates cryptid reports based on 'vibe-coding' principles for data quality."""
    def __init__(self, min_desc_length: int = 50, min_image_clarity: int = 6, min_witnesses: int = 2):
        self.min_desc_length = min_desc_length
        self.min_image_clarity = min_image_clarity
        self.min_witnesses = min_witnesses

    def evaluate_report(self, report: CryptidReport) -> dict:
        """
        Evaluates a cryptid report based on "vibe-coding" principles for data quality.
        This simulates rejecting "Bigfoot blurs" by setting clear criteria for robustness.
        """
        quality_score = 0
        feedback = []

        # --- Vibe-Coding Principle: Detailed Description for Clarity ---
        if len(report.description) >= self.min_desc_length:
            quality_score += 4
            feedback.append("Description is sufficiently detailed.")
        else:
            feedback.append(f"Description is too short (needs at least {self.min_desc_length} chars).")

        # --- Vibe-Coding Principle: Clear Evidence (Image Clarity) ---
        if report.image_clarity_score >= self.min_image_clarity:
            quality_score += 3
            feedback.append(f"Image clarity score ({report.image_clarity_score}/10) is good.")
        else:
            # This represents a 'Bigfoot blur' or unclear evidence
            feedback.append(f"Image clarity score ({report.image_clarity_score}/10) is low, potentially a 'Bigfoot blur'.")

        # --- Vibe-Coding Principle: Corroboration (Multiple Witnesses) ---
        if report.num_witnesses >= self.min_witnesses:
            quality_score += 3
            feedback.append(f"Sufficient number of witnesses ({report.num_witnesses}).")
        else:
            feedback.append(f"Few witnesses ({report.num_witnesses}), needs more corroboration.")

        # Determine overall quality based on the accumulated score
        if quality_score >= 8: # High quality threshold
            overall_status = "HIGH QUALITY - Accepted"
        elif quality_score >= 5: # Medium quality, might need review
            overall_status = "MEDIUM QUALITY - Needs Review"
        else: # Low quality, likely a "Bigfoot blur" and rejected
            overall_status = "LOW QUALITY - Rejected (Bigfoot Blur)"

        return {
            "overall_status": overall_status,
            "quality_score": quality_score,
            "feedback": feedback
        }

# --- Main execution --- 
if __name__ == "__main__":
    print("--- Cryptid Reporting Station: Data Quality Evaluation ---")

    # Initialize the evaluator with specific quality thresholds
    evaluator = ReportQualityEvaluator(
        min_desc_length=70,
        min_image_clarity=7,
        min_witnesses=2
    )

    # Example 1: A high-quality report
    report1 = CryptidReport(
        cryptid_name="Nessie",
        location="Loch Ness, Scotland",
        description="I saw a large, serpentine creature with humps moving gracefully across the water near Urquhart Castle. It was dark green and approximately 20 feet long. I managed to get a clear, albeit distant, photo.",
        image_clarity_score=8,
        num_witnesses=3,
        reporter_name="Dr. Fiona Campbell"
    )

    # Example 2: A low-quality report (Bigfoot blur)
    report2 = CryptidReport(
        cryptid_name="Bigfoot",
        location="Pacific Northwest Forest",
        description="Saw something big and hairy in the woods. It was fast.",
        image_clarity_score=3,
        num_witnesses=1,
        reporter_name="Hunter Joe"
    )

    # Example 3: A medium-quality report
    report3 = CryptidReport(
        cryptid_name="Chupacabra",
        location="Rural Texas",
        description="Found several livestock with strange puncture wounds. No clear sighting of the creature, but the damage is consistent with previous reports. Neighbors also reported unusual sounds last night.",
        image_clarity_score=5, # No direct image of creature, but evidence context
        num_witnesses=4,
        reporter_name="Rancher Bob"
    )

    reports = [report1, report2, report3]

    for i, report in enumerate(reports):
        print(f"\n--- Processing Report {i+1} ---")
        print(report)
        evaluation_result = evaluator.evaluate_report(report)
        print("\n--- Evaluation Result (Vibe-Coding for Quality) ---")
        print(f"Overall Status: {evaluation_result['overall_status']}")
        print(f"Quality Score: {evaluation_result['quality_score']}/10")
        print("Feedback:")
        for line in evaluation_result['feedback']:
            print(f"  - {line}")
        print("-" * 40)
