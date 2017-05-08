from django.db import models

# Create your models here.


from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=64, verbose_name="姓名")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserProfileManager()
    host_to_remote_users = models.ManyToManyField('HostToRemoteUser',)
    # 用户和远程登录用户简练多对多关联
    host_groups = models.ManyToManyField('HostGroups',)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email


class Host(models.Model):
    '''主机表'''
    hostname = models.CharField(max_length=64, unique=True, verbose_name='主机名')

    ip_addr = models.GenericIPAddressField()
    #
    port = models.SmallIntegerField(default=22)
    #     端口号
    idc = models.ForeignKey('IDC', blank=True, null=True)
    system_type_choice = ((1, 'Linux'), (2, "Windows"),)
    # 系统类型
    system_type = models.SmallIntegerField(choices=system_type_choice, verbose_name='系统类型')
    memo = models.CharField(max_length=128, blank=True, null=True, verbose_name='备注')
    #     备注
    enabled = models.BooleanField(default=1, verbose_name='启动北京权力')

    class Meta:
        unique_together = ('ip_addr', 'port')
        verbose_name = '主机表'

    def __str__(self):
        return "%s------>(%s)" % (self.hostname, self.ip_addr)


class IDC(models.Model):
    '''机房'''
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class RemoteUser(models.Model):
    '''远程主机使用用户'''
    auth_type_choices = ((1, 'ssh-password'), (2, "ssh-key"))
    auth_type = models.SmallIntegerField(choices=auth_type_choices, default=1)
    username = models.CharField(max_length=64, )
    password = models.CharField(max_length=256, help_text='如果您选取的事ssh-key，请键入密码')

    def __str__(self):
        return self.username

    class Meta:
        unique_together = ('auth_type', 'username', 'password')


class HostToRemoteUser(models.Model):
    # 手动创建多对多第三张表
    host = models.ForeignKey('Host')
    remote_user = models.ForeignKey('RemoteUser')

    def __str__(self):
        return '%s:%s' % (self.host, self.remote_user)

    class Meta:
        unique_together = ('host', 'remote_user')


class HostGroups(models.Model):
    """存储主机组"""
    name = models.CharField(max_length=64, unique=True)
    host_to_remote_users = models.ManyToManyField('HostToRemoteUser')
    #  和远程操作用户建立关联
    def __str__(self):
        return self.name


class AuditLog(models.Model):
    """存储审计日志"""
    user=models.ForeignKey('UserProfile',verbose_name="堡垒机账号",blank=True,null=True)
    host_to_remote_user=models.ForeignKey("HostToRemoteUser",null=True,blank=True)
    log_type_choices = ((0,'login'),(1,'cmd'),(2,'logout'))
    log_type=models.SmallIntegerField(choices=log_type_choices)
    content=models.CharField(max_length=255,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return "%s %s"%(self.host_to_remote_user,self.content)