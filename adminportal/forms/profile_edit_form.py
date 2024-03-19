# from django  import  forms 
# from website.models  import Company  
# class ProfileEditForm(forms.Form):
#     name = forms.CharField(max_length=254)
#     email = forms.EmailField(max_length=254) 
#     phone = forms.CharField(max_length=254)
#     twitter = forms.CharField(max_length=254 )
#     facebook = forms.CharField(max_length=254)
#     linkedin = forms.CharField(max_length=254)
#     instagram = forms.CharField(max_length=254)



    
#     class Meta:
#         fields = "__all__"
        
#     def errors_array(self):
#         return [f"{field} : ({error}"for field ,error_list in self.errors.items() for error in error_list]

#     def save(self):
#             company = Company.objects.all().last()

#             company.email = self.cleaned_data.get('email')
#             company.phone = self.cleaned_data.get('phone')
#             company.name = self.cleaned_data.get('name')
#             company.facebook = self.cleaned_data.get('facebook')
#             company.twitter = self.cleaned_data.get('twitter')
#             company.linkedin = self.cleaned_data.get('linkedin')
#             company.instagram = self.cleaned_data.get('instagram')
#             company.save()
#             return company