from django.shortcuts import render, redirect
from django.urls import reverse
import homepage
from product.models import Product
from .forms import Order as Order_Form
from .models import Orders
from confirmation.models import Confirmations_link

# Create your views here.

def Order(request, product_type=None, product_link=None):
    ctx = homepage.views.base_context()
    ctx["title"] = "Hudini"
    ctx["nav_name"] = "order"
    product_to_order = None
    for prod in Product.objects.filter(product_type=product_type):
        if prod.get_link() == product_link:
            product_to_order = prod
            break

    form = Order_Form(request.POST or None)
    success = False
    if request.method == 'POST':
        if form.is_valid():
            order = model_instance = form.save(commit=False)
            setattr(order, "product", product_to_order)
            order.save()
            link = str(request.META['HTTP_HOST']) + Confirmations_link.NewLink(order)

            from django.core.mail import EmailMultiAlternatives as Mail
            email = Mail('Potwierdzenie zamówienia', to=[order.email])
            email.attach_alternative(mail_confirmatioin(order, link), "text/html")
            email.send()

            return Success(request, ctx, order)

    ctx.update( {"form":form, "product" : product_to_order } )

    if product_to_order == None:
        return render(request, "order_not_found.html", {"product":product_link})
    return render(request, "order_form.html", ctx)

def Success(request, ctx, order=None):
    ctx.update({"order":order})
    return render(request, "success.html", ctx)



def mail_confirmatioin(order, link):    
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
                                                        Dzień dobry,</td>
                                                </tr>
                                                <tr>
                                                    <td colspan="3" style="font-family:Arial,sans-serif;width:100%;font-size:14px;color:#4d4d4d;padding:16px 0 40px 0" width="100%">
                                                        <div>
                                                            Potwierdź zamówienie """
    middle = str(order.count) + "x " + str(order.product.product_type) + ' "' + order.product.title + '" za łączną cenę (nie wliczając cany dostawy) '+ str(round((order.count * order.product.price), 2 )) + "zł</div><div>Na dane: <br>&nbsp;&nbsp;" + order.name +" "+ order.surname + "<br>&nbsp;&nbsp;tel. " + order.phone + "<br>&nbsp;&nbsp;ul." + order.adress +" " + order.house_number +"<br>&nbsp;&nbsp;miasto "+order.city_name+" "+order.zip_code
    end = """</div>
                                                            <div>
                                                                &nbsp;</div>
                                                            <div>
                                                                Aby potwierdzić zamówienie kliknij poniższy link:</div>
                                                            <div>
                                                                <a href='""" + "https://"+str(link) + "' target='_blank'>" + "https://"+str(link) + """</a></div>
                                                                lub<br>
                                                                <a href='""" + "http://"+str(link) + "' target='_blank'>" + "http://"+str(link) + """</a><br>
                                                               
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td colspan="5" style="font-family:Arial,sans-serif;width:100%" width="100%">
                                                            <table border="0" cellpadding="0" cellspacing="0" style="font-family:Arial,sans-serif;margin:0;padding:0;width:100%" width="100%">
                                                                <tbody>
                                                                    <tr>
                                                                        <td colspan="5" style="font-family:Arial,sans-serif;width:100%;font-family:Arial,sans-serif;font-size:14px;color:#4d4d4d;padding:30px 0 0 0" width="100%">
                                                                            <table border="0" cellpadding="0" cellspacing="0" style="font-family:Arial,sans-serif;margin:0;padding:0;width:100%" width="100%">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td colspan="5" height="2" style="width:100%;padding:0 0 0 0;height:2px;line-height:2px" width="100%">
                                                                                            <table border="0" cellpadding="0" cellspacing="0" height="2" style="margin:0;padding:0;width:100%;height:2px" width="100%">
                                                                                                <tbody>
                                                                                                    <tr>
                                                                                                        <td height="2" style="height:2px;width:10%;line-height:2px" width="10%">
                                                                                                            <div style="height:2px;width:100%;background-color:#1d1d1e;line-height:2px">
                                                                                                                &nbsp;</div>
                                                                                                        </td>
                                                                                                        <td height="2" style="line-height:2px;height:2px" width="10%">
                                                                                                            <div style="height:2px;background-color:#8a919a;width:100%;line-height:2px">
                                                                                                                &nbsp;</div>
                                                                                                        </td>
                                                                                                        <td height="2" style="height:2px;width:80%;line-height:2px" width="80%">
                                                                                                            <div style="height:2px;background-color:#d8dbe6;width:100%;line-height:2px">
                                                                                                                &nbsp;</div>
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
                                                                    <tr>
                                                                        <td colspan="2" style="font-family:Arial,sans-serif;width:40%;font-size:14px;color:#4d4d4d;padding:20px 0 14px 0" width="40%">
                                                                            Pozdrawiam serdecznie,<br>
                                                                            Hudini
                                                                        <td colspan="1" style="font-family:Arial,sans-serif;width:20%" width="20%">
                                                                            &nbsp;</td>
                                                                        <td colspan="2" style="font-family:Arial,sans-serif;width:40%;font-size:11px;color:#4d4d4d;padding:0 0 14px 0" width="40%">
                                                                            <table border="0" cellpadding="0" cellspacing="0" style="font-family:Arial,sans-serif;margin:0;padding:0;width:100%" width="100%">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td style="font-family:Arial,sans-serif;width:25%" width="25%">
                                                                                            <a href="https://www.facebook.com/hudinimusic/?eid=ARAt5gkM9LPXBfmKNGuMFPbXLnNWmj7WmQqeAtKcP7wy8ADe919bNBwIfxoAIUljy3pcsmoj3dRs1GSe" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.facebook.com/XKOMpl&amp;source=gmail&amp;ust=1587991857841000&amp;usg=AFQjCNEkBa1ye0EKR7loRxj095FtT9Q_AQ"><img alt="" src="https://ci4.googleusercontent.com/proxy/7RfH8FqEvHq67g2W7ffS1nFw1NK-s9L_SD62Sie6kHf54sfOA_wbk2qTFFina_7Uefmz82zbQjnZuyI8EHo=s0-d-e1-ft#http://stati.pl/allegro/powiadomienia/f.png" class="CToWUd"></a></td>
                                                                                        <td style="font-family:Arial,sans-serif;width:25%" width="25%">
                                                                                            <a href="https://www.youtube.com/channel/UCmj1LrkMPIJOdh3W0iMHm2w?view_as=subscriber" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.youtube.com/channel/UCmsxFRm1zRgueucG2Pc9Kzg&amp;source=gmail&amp;ust=1587991857842000&amp;usg=AFQjCNEYEO7ucDJQFUwU7jRBdZOqG8Zx_A"><img alt="" src="https://ci3.googleusercontent.com/proxy/u4pQxaHyvjRuT3uPwwJyLeEkCK7bFF9_7V37vvFGYeSsRHc6mu8GTrQHFD6sNUEumFeSIvk0cjPH8RZndFA=s0-d-e1-ft#http://stati.pl/allegro/powiadomienia/y.png" class="CToWUd"></a></td>
                                                                                        <td style="font-family:Arial,sans-serif;width:25%" width="25%">
                                                                                            <a href="https://instagram.com/szymihudini" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://instagram.com/xkompl/&amp;source=gmail&amp;ust=1587991857843000&amp;usg=AFQjCNF5CgMFfrodiuEXMASXabR28z6D7A"><img alt="" src="https://ci3.googleusercontent.com/proxy/hEu5UaS0vMsfam78clpxdaL1SHrDo8R1CExyLTYk-9Uy4LxKvQdW9kpzCKusf1rZsgSlJHGzzZzTiYXw6Sg=s0-d-e1-ft#http://stati.pl/allegro/powiadomienia/i.png" class="CToWUd"></a></td>
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
                        </td>
                    </tr>
                </tbody>
            </table>
            <p>
                &nbsp;</p><div class="yj6qo"></div><div class="adL">
            </div></div><div class="adL">


            </div></div></div><div id=":18z" class="ii gt" style="display:none"><div id=":17s" class="a3s aXjCH undefined"></div></div><div class="hi"></div></div>         """


    return head + middle + end