import os
import boto3
import eel
path="C:/Users/poweRadmIN/.aws"
@eel.expose
def register(pname,acc,sec,r,o):
    try:
        os.mkdir(path)
    except FileExistsError:
        print()
    cpath=path+"/config"
    cepath=path+"/credentials"
    p_name=pname
    a_id=acc
    s_key=sec
    region=r
    out_for=o
    file = open(cpath,"a+")
    file.write('[profile '+p_name+']')
    file.write('\n')
    file.write('region '+'='+' '+region)
    file.write('\n')
    file.write('output '+'='+' '+out_for)
    file.write('\n')
    file.close()
    file1 = open(cepath,"a+")
    file1.write("["+p_name+"]")
    file1.write("\n")
    file1.write("aws_access_key_id = "+a_id)
    file1.write("\n")
    file1.write("aws_secret_access_key = "+s_key)
    file1.write("\n")
    print("successfully createad a local file")
@eel.expose
def fuck():
    print("something")
    eel.init('www', allowed_extensions=['.js', '.html'])
    aws_mag_con=boto3.session.Session(profile_name="root")
    ec2_client = aws_mag_con.client('ec2', region_name='us-east-2') # Change as appropriate
    images = ec2_client.describe_images(Owners=['amazon'],Filters=[{'Name': 'image-type','Values': ['machine']},{'Name':'architecture','Values':['x86_64','arm64']}])['Images']
    for des in images:
        if des['PlatformDetails']=="Windows":
            eel.find_ami(des['ImageId'],des['Name'])   # Call a Javascript function
            print(des['ImageId'],des['Name'])
    ec2 = aws_mag_con.client('ec2')
    response = ec2.describe_instance_type_offerings()['InstanceTypeOfferings']
    for itype in response:
        eel.find_InsType(itype['InstanceType'])
    eel.start('xyz.html')

@eel.expose
def launch(image,Ins_type,min,max,region):
    aws_mag_con=boto3.session.Session(profile_name="root")
    ec2_resource = aws_mag_con.resource('ec2', region_name=region)
    instances = ec2_resource.create_instances(
        ImageId=image,
        MaxCount=int(max),
        MinCount=int(min),
        InstanceType=Ins_type)
@eel.expose
def Tab_Data():
     aws_mag_con=boto3.session.Session(profile_name="root")  
     ec2_cli=aws_mag_con.client('ec2')
     res=ec2_cli.describe_instances()['Reservations']
     for a in res:
        for b in a['Instances']:
            eel.desc(b['InstanceId'],b['State']['Name'])  
@eel.expose
def stopping_inst(x):
    aws_mag_con=boto3.session.Session(profile_name="root")  
    ec2_cli=aws_mag_con.client('ec2')
    ec2_cli.stop_instances(InstanceIds=[x])
@eel.expose
def starting_inst(c):
    aws_mag_con=boto3.session.Session(profile_name="root")  
    ec2_cli=aws_mag_con.client('ec2')
    ec2_cli.start_instances(InstanceIds=[c])
@eel.expose
def terminating_inst(d):
    aws_mag_con=boto3.session.Session(profile_name="root")  
    ec2_cli=aws_mag_con.client('ec2')
    ec2_cli.terminate_instances(InstanceIds=[d])

eel.init("www")
eel.start("test.html")
