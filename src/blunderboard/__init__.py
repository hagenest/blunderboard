from blunderboard.blunderevaluator import BlunderEvaluator
from blunderboard.boardreader import BoardReader
from blunderboard.movegenerator import MoveGenerator
from time import sleep
import cProfile


def main_content():
    blunder_evaluator = BlunderEvaluator()
    move_generator = MoveGenerator(blunder_evaluator)
    reader = BoardReader(move_generator)
    reader.scan()
    reader.print()
    while True:
        reader.scan()
        sleep(0.1)


def main():
    cProfile.run("main_content()")


# run main with cProfile
cProfile.run("main()")
