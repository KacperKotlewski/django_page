from django.shortcuts import render, redirect
from .models import Confirmations_link
import homepage

# Create your views here.
def Confirm(request, confirmation_link=None):
    ctx = homepage.views.base_context()
    ctx["title"] = "Hudini"
    ctx["nav_name"] = "order"

    conf = None
    if Confirmations_link.objects.filter(link=confirmation_link).count != 0:
        conf = Confirmations_link.objects.filter(link=confirmation_link)[0]
    order = conf.order
    if conf != None and order.is_confirmed == False:
        order.is_confirmed = True
        order.save(update_fields=['is_confirmed'])
        ctx.update({"order":order})

        from django.core.mail import EmailMultiAlternatives as Mail
        email = Mail('Potwierdzenie zamówienia', to=["testmail@gmail.com"])
        email.attach_alternative(mail_confirmatioin(order), "text/html")
        email.send()

        return render(request, "confirmed.html", ctx)
    else: 
        return redirect("homepage") 

def mail_confirmatioin(order):    
    head = """<div class=""><div class="aHl"></div><div id=":18l" tabindex="-1"></div><div id=":186" class="ii gt"><div id=":lq" class="a3s aXjCH "><div class="adM">
        </div><div style="font-family:Geneva,Helvetica,Arial,sans-serif;font-size:12px"><div class="adM">
        </div><table border="0" cellpadding="0" cellspacing="0" style="font-family:Arial,sans-serif;margin:0;padding:0;width:100%" width="100%">
            <tbody>
                <tr>
                    <td align="center" bgcolor="#e3e3e3" style="font-family:Arial,sans-serif;width:100%" valign="top" width="100%">
                        <table border="0" cellpadding="0" cellspacing="0" style="font-family:Arial,sans-serif;margin:20px;padding:0;max-width:700px" width="700">
                            <tbody>
                                <tr>
                                    <td align="center" bgcolor="#ffffff" style="font-family:Arial,sans-serif;width:700px;border-radius:15px;padding:20px;margin:20px auto" valign="top" width="700">
                                        <table border="0" cellpadding="0" cellspacing="0" style="font-family:Arial,sans-serif;margin:0;padding:0;max-width:700px;width:100%" width="100%">
                                            
                                            <tbody>
                                                <tr>
                                                    <td colspan="3" style="font-family:Arial,sans-serif;width:100%;font-size:24px;color:#4d4d4d;padding:10px 0 0 0" width="100%">
                                                        Nowe zamówienie</td>
                                                </tr>
                                                <tr>
                                                    <td colspan="3" style="font-family:Arial,sans-serif;width:100%;font-size:14px;color:#4d4d4d;padding:16px 0 40px 0" width="100%">
                                                        <div>
                                                            """
    middle = str(order.count) + "x " + str(order.product.product_type) + ' "' + order.product.title + '" za łączną cenę (nie wliczając cany dostawy) '+ str(round((order.count * order.product.price), 2 )) + "zł</div><div>Na dane: <br>&nbsp;&nbsp;" + order.name +" "+ order.surname + "<br>&nbsp;&nbsp;tel. " + order.phone + "<br>&nbsp;&nbsp;ul." + order.adress +" " + order.house_number +"<br>&nbsp;&nbsp;miasto "+order.city_name+" "+order.zip_code
    end = """</div></td>
                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
            <p>
                &nbsp;</p><div class="yj6qo"></div><div class="adL">
            </div></div><div class="adL">


            </div></div></div><div id=":18z" class="ii gt" style="display:none"><div id=":17s" class="a3s aXjCH undefined"></div></div><div class="hi"></div></div>         """


    return head + middle + end