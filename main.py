from input_verb import inputVerb
from simple_times import SimpleTime 
from composed_times import ComposedTime

verb = inputVerb()

verbSimpleTime = SimpleTime(verb=verb)
verbSimpleTime.conjugateAllTimes()

verbComposedTime = ComposedTime(verb=verb)
verbComposedTime.conjugateAllTimes()


