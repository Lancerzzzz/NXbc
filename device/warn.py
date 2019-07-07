from django.core.mail import send_mail

from device.models import receivelist


class sendmail(object):
    def get(self):
        headline = "Subject"
        content = "hello"
        SourEmail = "15606924217@163.com"
        TarEmail = ['355919474@qq.com', '1652085034@qq.com']
        # TarEmail = ['xzl520vip@qq.com']
        send_mail(headline, content, SourEmail,
                  TarEmail, fail_silently=False)

        return True


class receiveList(object):
    def get(self):
        tarList = receivelist.objects.values()
        print("tarList:", tarList)
        tarJson = {}
        tar = []
        for i in tarList:
            tar.append(i)
        tarJson['info'] = tar
        print("tarJson:", tarJson)
        return tarJson


class delTar(object):
    def get(self):
        tarDel = receivelist.objects.filter(emailaccount='123456789@qq.com').delete()
        tarList = receivelist.objects.values()
        print("tarList:", tarList)
        tarJson = {}
        tar = []
        for i in tarList:
            tar.append(i)
        tarJson['info'] = tar
        print("tarJson:", tarJson)
        return tarJson


class createTar(object):
    def get(self):
        tarCreate = receivelist.objects.create(emailaccount='123456789@qq.com')
        tarCreate.save()
        tarList = receivelist.objects.values()
        print("tarList:", tarList)
        tarJson = {}
        tar = []
        for i in tarList:
            tar.append(i)
        tarJson['info'] = tar
        print("tarJson:", tarJson)
        return tarJson


if __name__ == "__main__":
    sendMail = sendmail()
    sendMail.get()
