
def eval_parser(run, example):

    #gt = example.outpus or {}
    gt = example.outputs or {}

    gt_outbound_date = gt['outbound_date']

    param = run.outputs or {}
    if not isinstance(param, dict):
        param.model_dump()

    pred = param['flight_params']

    pred_outbound = pred['outbound_date']

    score = 1 if pred_outbound == gt_outbound_date else 0

    return {
        'key' : 'parser',
        'score': score,
        'comment': f'Outbound actual {gt_outbound_date} and Outbound predicted {pred_outbound}'
    }




    
   