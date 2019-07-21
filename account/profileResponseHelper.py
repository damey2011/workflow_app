from rest_framework.response import Response

def get_api_response(profile_status=1, data={}, errors={}, httpStatusCode= 200):
    '''Returns a response object'''
    response_data = {"status":profile_status, "description": ProfileStatusCodesDescription[profile_status], "data": data, "errors":errors}   

    return Response(data=response_data, status=httpStatusCode)

class ProfileStatusCodes:
    Success = 1
    Invalid_Field = 2,
    Profile_Pic_Size_Exceeded = 3
    

ProfileStatusCodesDescription = {
    ProfileStatusCodes.Success:"Success", 
    ProfileStatusCodes.Invalid_Field:"Some fields are invalid",
    ProfileStatusCodes.Profile_Pic_Size_Exceeded:"Picture size limit exceeded",
}