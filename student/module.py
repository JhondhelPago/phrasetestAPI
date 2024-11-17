def get_unfinished_essay_assignment_id(all_essay_assignment_ids, done_essay_assignment_ids):

    return [essay_assignment_id for essay_assignment_id in all_essay_assignment_ids if essay_assignment_id not in done_essay_assignment_ids]

    
