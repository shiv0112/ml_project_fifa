from fifa_rating.pipeline.pipeline import Pipeline
from fifa_rating.exception import FifaException
import sys,os


def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        raise FifaException(e, sys) from e
        

if __name__ == '__main__':
    main()
