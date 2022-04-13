# coding: utf-8
#
# Copyright 2018 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.]

"""Domain objects for topics, and related models."""

from __future__ import annotations

import copy
import datetime
import functools
import json
import re

from core import android_validation_constants
from core import feconf
from core import utils
from core.constants import constants
from core.domain import change_domain, user_domain
from core.domain import fs_domain
from core.domain import story_domain
from core.domain import topic_domain
from core.domain import skill_domain

from typing import List, Optional, Type
from typing_extensions import TypedDict

class UserProgressInSubtopicDict(TypedDict):
    """Dictionary representation of user's progress in a subtopic."""

    subtopic: topic_domain.Subtopic
    progress_in_skills: List[skill_domain.UserSkillMastery]


class UserProgressInStoryDict(TypedDict):
    """Dictionary representation of user's progress in a story."""

    story_id: str
    completed_story_nodes: List[story_domain.StoryNode]
    incomplete_story_nodes: List[story_domain.StoryNode]
    all_story_nodes: List[story_domain.StoryNode]


class LearnerGroupUserProgressDict(TypedDict):
    """Dictionary representation of user progress for a learner group."""

    group_id: str
    progress_in_subtopics: List[UserProgressInSubtopicDict]
    progress_in_stories: List[UserProgressInStoryDict]


class LearnerGroupStorySummaryDict(TypedDict):
    """Dictionary representation of Learner Group Story Summary."""

    story_id: str
    title: str
    description: str
    language_code: str
    thumbnail_bg_color: str
    thumbnail_filename: str
    url_fragment: str
    story_nodes: List[story_domain.StoryNode]
    topic_id: str
    topic_name: str
    topic_url_fragment: str
    classroom_url_fragment: str


class LearnerGroupSummaryDict(TypedDict):
    """Dictionary representation of Learner Group Summary."""

    group_id: str
    title: str
    description: str
    subtopic_summaries: List[topic_domain.Subtopic]
    story_summaries: List[LearnerGroupStorySummaryDict]

class LearnerGroupUser:
    """Domain object for learner group's user."""

    def __init__(
            self, user_id: str, username: str,
            progress_in_subtopics: List[UserProgressInSubtopicDict],
            progress_in_stories: List[UserProgressInStoryDict]):
        """Constructs a LearnerGroupUser domain object.

        Args:
            user_id: str. The unique ID of the user.
            username: str. Identifiable username to display in the UI.
            progress_in_subtopics: list(UserProgressInSubtopicDict). The
                progress of user in subtopics of the learner group.
            progress_in_stories: list(UserProgressInStoryDict). The progress
                of user in the stories of the learner group.
        """
        self.user_id = user_id
        self.username = username
        self.progress_in_subtopics = progress_in_subtopics
        self.progress_in_stories = progress_in_stories

    def to_dict(self) -> LearnerGroupUserProgressDict:
        """Returns a dict representation of the LearnerGroupUserProgress domain
        object.
        """
        return {
            'group_id': self.group_id,
            'progress_in_subtopics': [
                progress.to_dict() for progress in self.progress_in_subtopics],
            'progress_in_stories': [
                progress.to_dict() for progress in self.progress_in_stories]
        }

    @classmethod
    def from_dict(cls, learner_group_user_progress_dict: LearnerGroupUserProgressDict) -> LearnerGroupUserProgress:
        """Returns a LearnerGroupUserProgress domain object from a dict.

        Args:
            learner_group_user_progress_dict: dict. The dict representation of
                LearnerGroupUserProgress object.

        Returns:
            LearnerGroupUserProgress. The corresponding LearnerGroupUserProgress
            domain object.
        """
        # return cls(
        #     learner_group_user_progress_dict['group_id'],
        #     [UserProgressInSubtopic.from_dict(progress)
        #      for progress in learner_group_user_progress)


class LearnerGroupSyllabus:
    """Domain object for learner group syllabus"""
    def __init__(
        self, subtopic_summaries: List[topic_domain.Subtopic],
        story_summaries: List[LearnerGroupStorySummaryDict]):
        """Constructs a LearnerGroupSyllabus domain object.

        Args:
            subtopic_summaries: list(topic_domain.Subtopic). The summary
                subtopics(collection of skills in syllabus) in
                the learner group.
            story_summaries: list(LearnerGroupStorySummaryDict). The summary
                of stories in the learner group.
        """
        self.subtopic_summaries = subtopic_summaries
        self.story_summaries = story_summaries

class LearnerGroup:
    """Domain object for learner group."""

    def __init__(
            self, group_id: str, title: str, description: str,
            invitations: List[user_domain.UserSettings],
            members: List[LearnerGroupUser],
            syllabus: LearnerGroupSyllabus):
        """Constructs a LearnerGroupSummary domain object.

        Args:
            group_id: str. The id of the learner group.
            title: str. The title of the learner group.
            description: str. The description of the learner group.
            invitations: list(tuser_domain.UserSettings). Info about the
                learners invited to join the learner group.
            members: list(LearnerGroupUser). Info about the members of the
                learner group and their progress through the syllabus.
            syllabus: list(LearnerGroupSyllabus). The syllabus
                of the learner group.
        """
        self.group_id = group_id
        self.title = title
        self.description = description

    def to_dict(self) -> LearnerGroupSummaryDict:
        """Returns a dict representation of the LearnerGroupSummary domain
        object.
        """
        return {
            'group_id': self.group_id,
            'title': self.title,
            'description': self.description,
            'subtopic_summaries': [
                subtopic.to_dict() for subtopic in self.subtopic_summaries],
            'story_summaries': [
                story.to_dict() for story in self.story_summaries]
        }

    @classmethod
    def from_dict(cls, learner_group_summary_dict: LearnerGroupSummaryDict) -> LearnerGroup:
        """Returns a LearnerGroupSummary domain object from a dict.

        Args:
            learner_group_summary_dict: dict. The dict representation of
                LearnerGroupSummary object.

        Returns:
            LearnerGroupSummary. The corresponding LearnerGroupSummary domain
            object.
        """
        return cls(
            learner_group_summary_dict['group_id'],
            learner_group_summary_dict['title'],
            learner_group_summary_dict['description'],
            [topic_domain.Subtopic.from_dict(subtopic)
             for subtopic in learner_group_summary_dict['subtopic_summaries']],
            [LearnerGroup.from_dict(story)
             for story in learner_group_summary_dict['story_summaries']]
        )

