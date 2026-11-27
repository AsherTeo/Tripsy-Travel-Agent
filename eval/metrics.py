from eval.api import find_real_flight

def eval_parser(run, example):

    gt = example.outputs or {}
    param = run.outputs or {}

    if not isinstance(param, dict):
        param.model_dump()

    pred = param['flight_params']

    score = 0 
    lst = []

    parameters = ["outbound_date", "return_date", "travel_class", "type"]

    for p in parameters:
        gt_param = gt[p]
        pred_param = pred[p]

        if gt_param == pred_param :
            score += 1
        lst.append(f'{p} actual {gt_param} and {p} predicted {pred_param}')


    return {
        'key' : 'parser',
        'score': score/ len(parameters), 
        'comment': ' | '.join(lst),   
    }


def eval_result(run, example):

    param = run.outputs or {}

    if not param or not param['flight_outbound_picked']:
        return {"key": "flight_result", "score": None, "comment": "There is no flight"}
    
    flights = param['flight_outbound_picked']['flights'][0]

    if not flights or not flights.get('flight_number', None):
        return {"key": "flight_result", "score": None, "comment": "There is no flight number"}

    outbound_date = flights['departure_airport']['time'].split(' ')[0]
    
    flight_code = flights.get('flight_number').replace(' ', '').lower() 
    live_outputs = find_real_flight(flight_code, outbound_date)

    if live_outputs == []:
        return {'key': 'flight_result', 'score': 0, 'comment': 'no flight exist'} 

    API_output = {
            'outbound_date':outbound_date,
            'outbound_time': flights['departure_airport']['time'].split(' ')[1] ,
            'departure_id': flights['departure_airport']['id'],
            'arrival_id':flights['arrival_airport']['id'],
    }

    score = 0 
    lst = []

    for lo in live_outputs:
        for key, values in lo.items():
            if API_output[key] == values:
                score += 1
                lst.append(f'{key} live output {values} and {key} API output {API_output[key]}')

    return {'key': 'flight_result', 
            'score': score / 4, 
            'comment': ' | '.join(lst), 
        } 
   