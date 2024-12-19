import sys
import warnings
from crew import ResearchCrew

#!/usr/bin/env python


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run(topic):
    """
    Run the crew.
    """
    inputs = {"topic": topic}
    ResearchCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        topic = sys.argv[1]
        run(topic)
    else:
        print("Please provide a topic as a command line argument.")
