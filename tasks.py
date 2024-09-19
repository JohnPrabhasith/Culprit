from crewai import Task
from tools import *
from agents import *

Research_task = Task(
    description = (
        '''
        Identify the next big trend in {topic}.Focus in Identifying the pros and cons
        and the overall narrative.Your final report should clearly articulate the key points,
        its market opportunities, and potential risks.
        '''
    ),
    expected_output = 'A Comprehensive 13 paragraphs long report on the latest AI Trends',
    tools = [tool],
    agent = News_Researcher,
)

Write_task = Task(
    description = (
        '''
        Compose an insightful article on {topic}.Focus on the latest trends
        and how it's impacting the industry.This article should be easy to understand,engaging and positive.
        '''
    ),
    expected_output = 'A paragraph article on {topic} advancements in around 12 to 14 paragraphs formatted as markdown',
    tools = [tool],
    agent = News_Writer,
    async_execution = False,
    output_file = 'new-blog-post.md'
)
