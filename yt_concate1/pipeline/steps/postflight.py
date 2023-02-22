from yt_concate1.pipeline.steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postflight')
