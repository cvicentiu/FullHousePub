def basepath(request):
    return {
        'basepath':'/static/'
            }

from core.menu.models import MenuItem
def process_session_order(session):
    order = session.get('order', default=None)
    total = 0
    result = {'items':[], 'total':0}
    if not order:
        return result 
    for key, value in order.iteritems():
        try:
            item = MenuItem.objects.get(pk=key)
            result['items'].append((item.name, int(value), int(value) * item.price, key))
            total += int(value) * item.price
        except:
            pass
    result['total'] = total
    print result
    return result 

def session_order(request):
    return {
        'basket_goods':process_session_order(request.session)
        }
