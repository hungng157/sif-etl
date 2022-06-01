import json
from services.config import config_service
from services import database_service


def create_event_proposal_deposit_mutation(hash, event_type,
                                           events_arr, height, timestamp,
                                           sender, recipient, proposal_type, voting_period_start, token, amount, gasWanted, gasUsed):

    sql_str = '''
    INSERT INTO {13}
    (hash, type, log, height, time,
    pd_sender, pd_recipient, pd_proposal_type,
    pd_voting_period_start, pd_token, pd_amount,
    pd_gasWanted, pd_gasUsed)
    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', 
    '{5}', '{6}', '{7}', 
    '{8}', '{9}', '{10}',
    '{11}','{12}'
    )
    '''.format(hash, event_type, json.dumps(events_arr), height, timestamp,
               sender, recipient, proposal_type, voting_period_start,
               token, amount, gasWanted, gasUsed,
               config_service.schema_config['EVENTS_TABLE_V2'])

    database_service.execute_update(sql_str)
