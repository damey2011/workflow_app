from django.contrib.auth import get_user_model
from guardian.utils import get_anonymous_user
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from rest_framework.response import Response

from organization.permissions import IsOwnerOrReadOnly
from process.serializers import *


##############################################################################################
class ProcessList(generics.ListCreateAPIView):
    '''Sample request: {"organization":"1","process_name":"StudentReg","description":"Student Registration"}'''
    serializer_class = ProcessSerializer
    parser_classes = (MultiPartParser, FormParser,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['process_name']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)  # permission for authenticated users and owner of Organization

    def get_queryset(self):
        queryset = Process.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        serializer.save(user_id=user)


class ProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, modify or delete Process.'''
    queryset = Process.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = ProcessSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

##############################################################################################


class StageList(generics.ListCreateAPIView):
    '''Sample request: {"process":"3","order":"1"}'''
    serializer_class = StageSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)  # permission for authenticated users and owner of Organization

    def get_queryset(self):
        queryset = Stage.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        serializer.save(user_id=user)


class StageDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, modify or delete Stage.'''
    queryset = Stage.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = StageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

##############################################################################################


class TaskList(generics.ListCreateAPIView):
    '''Sample request: {"stage":"1","document":"3","form":"2","groups":"2","users":"2"}'''
    serializer_class = TaskSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)  # permission for authenticated users and owner of Organization

    def get_queryset(self):
        queryset = Tasks.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        serializer.save(user_id=user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, modify or delete Task.'''
    queryset = Tasks.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

##############################################################################################


class DocumentList(generics.ListCreateAPIView):
    '''Sample request: {"organization":"1","file":"cloudinary url"}'''
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser, FormParser, FileUploadParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)  # permission for authenticated users and owner of Organization

    def get_queryset(self):
        queryset = Document.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        # file = self.request.FILES['file']
        # if file:
        #     result = cloudinary.uploader.upload(file, 
        #                                         folder = "workflow801",
        #                                         overwrite = "true", 
        #                                         resource_type = "raw") #cloudinary file upload
        #     file_url = result['secure_url']  #store the public id cloudinary upload
        serializer.save(user_id=user)


class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, modify or delete Document.'''
    queryset = Document.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

##################################################################################################


class FormList(generics.ListCreateAPIView):
    '''Sample request: {"organization":"1","form_name":"1","description":"Form description","fields":"{form html elements}"}'''
    serializer_class = FormSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)  # permission for authenticated users and owner of Organization

    def get_queryset(self):
        queryset = Form.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        serializer.save(user_id=user)


class FormDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, modify or delete Form.'''
    queryset = Form.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = FormSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

####################################################################################################


class FormresponseList(generics.ListCreateAPIView):
    '''Sample request: {"form_id":"2","response":"Response"}'''
    serializer_class = FormresponseSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)  # permission for authenticated users and owner of Organization

    def get_queryset(self):
        queryset = Formresponse.objects.all()
        user = self.request.user if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        return queryset

    def perform_create(self, serializer):
        user = self.request.user.id if self.request.user.is_authenticated else get_anonymous_user()  # handling unauthorized access
        serializer.save(user_id=user)


class FormresponseDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, modify or delete Formresponse.'''
    queryset = Formresponse.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = FormresponseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

################################################################################################


@api_view(['POST'])
def processflow(request, format=None):
    '''Sample request: {"email":"ogbanugot@gmail.com","password":"mypass","first_name":"ogban","last_name":"ugot", "phone_number":"08092343839"}
    '''
    if request.user.is_authenticated:
        return Response(status=status.HTTP_200_OK)

    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        first_name = serializer.validated_data["first_name"]
        last_name = serializer.validated_data["last_name"]
        user = get_user_model().objects.create_user(email=email, username=email,
                                                    password=serializer.validated_data["password"],
                                                    first_name=first_name,
                                                    last_name=last_name)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


###############################################################################################################
@api_view(['POST'])
def processflow(request, format=None):
    '''
    Sample request: {
        "id": 1,
        "user_id":3,
        "stage": 4,
        "document": null,
        "form": 1,
        "groups": null,
        "users": null,
        "isComplete": false
    }
    '''
    # set isComplete in task True
    task_id = request.data.get("id")
    task = Tasks.objects.get(pk=task_id)
    task.isComplete = True
    task.save()
    # Get stage_id of the task
    stage_id = request.data.get("stage")
    stage = Stage.objects.get(pk=stage_id)
    # Get process_id of the stage
    process_id = stage.process.id
    # Get all the tasks in stage
    tasks_in_stage = Tasks.objects.filter(stage=stage_id)
    numberofTasks = len(tasks_in_stage)
    completeTasks = 0
    # check how many tasks are isComplete
    for task in tasks_in_stage:
        if task.isComplete == True:
            completeTasks += 1

    if completeTasks == numberofTasks:
        # if all the tasks in the stage are complete, set the stage to complete
        stage.isComplete = True
        stage.save()
        # check if all the stages in the process are complete
        stages_in_process = Stage.objects.filter(process=process_id)
        numberofStages = len(stages_in_process)
        completeStage = 0
        for stage in stages_in_process:
            if stage.isComplete == True:
                completeStage += 1
        # if all the stages in the process are complete, set process to complete
        if completeStage == numberofStages:
            process_data = Process.objects.get(pk=process_id)
            process_data.isComplete = True
            process_data.save()
        Response(status=status.HTTP_200_OK)

    else:
        Response(status=status.HTTP_200_OK)
