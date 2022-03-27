

def create_group(title, description, invitations, syllabus):
    """Creates a new learner group data model.

    Args:
        title: Title of the learner group to be created.
        description: Description of the learner group to be created.
        invitations: List of usersnames invited to join the learner group.
        syllabus: Syllabus of the learner group to be created.
                  It is a dictionary with 2 keys, skills and stories which
                  store a list of ids corresponding to all skills and stories
                  part of the group syllabus.

    Returns:
        The learner group data model created.
    """

def update_group(group_id, title, description, invitations, syllabus):
    """Updates an existing learner group data model.

    Args:
        group_id: Id of the learner group to be updated.
        title: Title of the learner group to be updated.
        description: Description of the learner group to be updated.
        invitations: List of usersnames invited to join the learner group.
        syllabus: Syllabus of the learner group to be updated.
                  It is a dictionary with 2 keys, skills and stories which
                  store a list of ids corresponding to all skills and stories
                  part of the group syllabus.

    Returns:
        The learner group data model updated.
    """

def delete_group(group_id):
    """Deletes an existing learner group data model.

    Args:
        group_id: Id of the learner group to be deleted.

    Returns:
        True or false based on success or failure of deletion of learner group.
    """

def get_facilitator_view_of_learner_group(group_id):
    """Fetches all data required for facilitator's view of a learner group.

    Args:
        group_id: Id of the learner group to be fetched.

    Returns:
        group_details and learner_progress where group details stores a
        dictionary of all learner group data and learner progress stores a
        dictionary of username as key and their skills and stories progress
        as values.
    """

def get_learner_view_of_learner_group(group_id):
    """Fetches all data required for learner's view of a learner group.

    Args:
        group_id: Id of the learner group to be fetched.

    Returns:
        group_details and learner_progress where group details stores a
        dictionary of all learner group data and learner progress stores a
        list of all skills and stories summary user models part of the group
        syllabus.
    """

def get_learner_progress_multi(group_id, usernames):
    """Fetches progress in group syllabus for the given list of usernames.

    Args:
        group_id: Id of the learner group for which progress is to be fetched.
        usernames: List of usernames of all learner's whose progress we 
        have to fetch.

    Returns:
        group_details and learner_progress where group details stores a
        dictionary of all learner group data and learner progress stores a
        list of all skills and stories summary user models part of the group
        syllabus.
    """

def update_invitations(group_id, username, has_accepted_invitation):
    """Adds learner as member of the group if the invitation was accepted
    or removes the username from the learner group invitaions if the invitation
    was rejected by the learner.

    Args:
        group_id: Id of the learner group whose invitaiton was accepted/rejected.
        username: Username of the learner who recieved the invitation.
        has_accepted_invitation: True if the invitaion was accepted and
        False if the invitation was rejected.
    """

def remove_learner(group_id, username):
    """Removes the learner from the group when the learner exits the learner
    group or the facilitator removes the leaner from the learner group.

    Args:
        group_id: Id of the learner group.
        username: Username of the learner who is to be removed.
    """

def get_filtered_stories_and_skills(group_id, filter_args):
    """Fetches and returns summaries of all skills and stories that can
    be added as group syllabus based on the filter arguments.

    Args:
        group_id: Id of the learner group.
        filter_args: A dictionary of 'keyword', 'type', 'category' and
        'language' which essentially store the keyword entered
        in the search bar(it is to be compared for stories, skills, topic
        names), the type of the filter to be applied from story or
        skill, category of skills and stories, specific language filter
        for which the skill or story is available.

    Returns:
        A dictionary of 'skills_summary_dicts' and 'stories_summary_dicts'
        which store a list of summaries of all skills and stories that
        match the filter.
    """

# add this section to skill_services.py


def get_filtered_skill_summaries_for_learner_group(filter_args):
    """
    Args:
        filter_args: A dictionary of 'keyword', 'category' and
        'language' which essentially store the keyword entered
        in the search bar(it is to be compared for skills names),
        category of skills required, specific language filter
        for which the skill is available.

    Returns:
        A list of summaries of all skills that
        match the filter.
    """

# Add this section to story services

def get_filtered_story_summaries_for_learner_group():
    """
    Args:
        filter_args: A dictionary of 'keyword', 'category' and
        'language' which essentially store the keyword entered
        in the search bar(it is to be compared for story and topic names),
        category of stories(essentially topics) required, specific language
        filter for which the story is available.

    Returns:
        A list of summaries of all stories that
        match the filter.
    """

# Add this section to user services

def update_learner_group_user(
    username, learner_groups, owner_of_learner_groups):
    """Updates the learner groups that the user belongs to and were
    created by the user.

    Args:
        username: Username of the learner group user to be updated.
        learner_groups: List of ids of all learner groups to which the user
        belongs.
        owner_of_learner_groups: List of ids of all learner groups
        created by the user.
    """

def update_learner_group_user_preferences(
    group_id, username, progress_sharing_choice):
    """
    Updates progress sharing permission of the learner for a particular
    learner group.

    Args:
        group_id: Id of the learner group.
        username: Username of the learner for whom the progress sharing
        permissions are to be updated
        progress_sharing_choice: Takes boolean values, true indicates
        that the progress sharing permissions for that group are turned on
        and false means they are turned off.
    """