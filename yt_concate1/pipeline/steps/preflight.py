from yt_concate1.pipeline.steps.step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('in preflight')
        utils.create_dir()
