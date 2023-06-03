    def clean(self):
        if self.type == 'Numeric':
            if self.num_min is None or self.num_max is None:
                raise ValidationError('Please enter min and max values for numeric question')
            elif self.num_min > self.num_max:
                raise ValidationError('Min value should be less than max value')
            elif self.text_answer is not None:
                raise ValidationError('Numeric question should not have text answer')
        elif self.type == 'Text':
            if self.num_min is not None or self.num_max is not None:
                raise ValidationError('Text question should not have min and max values')
            elif self.text_answer is None:
                raise ValidationError('Text question should have text answer')
        elif self.type == 'MCQ':
            if self.num_min is not None or self.num_max is not None:
                raise ValidationError('MCQ question should not have min and max values')
            elif self.text_answer is not None:
                raise ValidationError('MCQ question should not have text answer')
        elif self.type == 'SCQ':
            if self.num_min is not None or self.num_max is not None:
                raise ValidationError('SCQ question should not have min and max values')
            elif self.text_answer is not None:
                raise ValidationError('SCQ question should not have text answer')
 
