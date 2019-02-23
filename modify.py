import json
import os

titles = '''Introduction
The Characters of the Story
Attention and Effort
The Lazy Controller
The Associative Machine
Cognitive Ease
Norms, Surprises, and Causes
A Machine for Jumping to Conclusions
How Judgments Happen
Answering an Easier Question
The Law of Small Numbers
Anchors
The Science of Availability
Availability, Emotion, and Risk
Tom W's Specialty
Linda: Less is More
Causes Trump Statistics
Regression to the Mean
Taming Intuitive Predictions
The Illusion of Understanding
The Illusion of Validity
Intuitions Vs Formulas
Expert Intuition: When Can We Trust It?
The Outside View
The Engine of Capitalism
Bernoulli's Errors
Prospect Theory
The Endowment Effect
Bad Events
The Fourfold Pattern
Rare Events
Risk Policies
Keeping Score
Reversals
Frames and Reality
Two Selves
Life as a Story
Experienced Well-Being
Thinking About Life
Conclusions'''

title_array = titles.split('\n')

titleline = '<title>Thinking, Fast and Slow</title>'

counter = 0
for filename in os.listdir('./chapters'):
    if '.html' in filename:

        file = open('./chapters/'+filename, 'r', encoding='UTF-8')
        oldhtml = file.read()
        file.close()

        if titleline in oldhtml:
            file = open('./chapters/'+filename, 'w+', encoding='UTF-8')
            newhtml = oldhtml.replace(titleline, '<title>{} {}</title>'.format(counter+1, title_array[counter]))
            file.write(newhtml)
            file.close()
            print(filename+': title replaced')

        counter+=1

print('Done')