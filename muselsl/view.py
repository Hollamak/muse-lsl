
def view(window=5, scale=100, refresh=0.2, figure="15x6", version=1, backend='TkAgg',data_type="EEG",source_id=None):
    if version == 2:
        from . import viewer_v2
        viewer_v2.view(data_type,source_id)
    else:
        from . import viewer_v1
        viewer_v1.view(window, scale, refresh, figure, backend)
