---
layout: post
title: "Some comments regarding Spring VS Rails"
date: 2011-05-27 04:00:04 -0500
comments: true
categories:
---
For the starters, couple reasons that Spring is better than Ruby on Rails.
Reason1: Routes Service - Complex routers
Ruby on Rails
Given link:

{% raw %}
```
%a{:href => export_path} Export_Link
```
{% endraw %}





/config/routes.rb:
{% raw %}
```
   match ‘/export’ => ‘PatientController#exportservice’
$rake routes:
export /export(.:format) {:controller=>”PatientController”, :action=> ”export”}
/app/controller/patients_controller.rb:
Class Patientcontroller < ApplicationController
  def exportservice
    puts “export executed”  
  end
end
```
{% endraw %}

Spring
   Given link:
{% raw %}
```
<a href = ‘/dbo/patient/export.html’> Export_link </a>
```
{% endraw %}


/dbo/patientController.java:
{% raw %}
```
@Controller
@RequestMapping("/dbo/patient/\*")
public class PatientCOntroller extends AbstractDboController{
  @RequestMapping(value=”export.html”, method=RequestMethod(GET))
  public ModelAndView exportService(){
    System.out.println(‘exported excuted’);
    Return new ModelAndView(“dbo/patient/export.jsp”);
  }
}
```
{% endraw %}





Reason2: Database Service - ActiveRecord vs Hibernate
Ruby on Rails
{% raw %}
```
@patients = Patient.all
@patients.each do |patient|
    return paitent.paient_name
end
```
{% endraw %}

Spring
{% raw %}
```
@Autowired
private DboDaoService dboDaoService;
public String function(){
    return dboDaoService.getPatientService().getPaitent_Name();
}
```
{% endraw %}


Reason3: Model Initialization - Crazy ruby syntax
Ruby on Rails
app/model/patient.rb:

{% raw %}
```
class Patient < ActiveRecord :: Base
belongs_to :MRN
  def exportService
    return “activated”
  end
end
```
{% endraw %}


app/controller/patients_controller.rb:
{% raw %}
```
puts Patient.new.exportService
```
{% endraw %}


Spring
src/main/java/package/dbo/exporter/patient.java:

{% raw %}
```
@Service
public class Patient implements PetientService {
    public String exportService(){
        return “activated”;
    }
}
src/main/java/package/dbo/exporter/patientService.java:
public interface PatientService{
    public String exportService();
}
```
{% endraw %}

src/main/java/package//dbo/patientController.java:

{% raw %}
```
@Autowired
private patientService PatientService

@Controller
@RequestMapping(“/dbo/patient/\*”)
public class PatientCOntroller extends AbstractDboController{
  @RequestMapping(value=”export.html”, method=RequestMethod(GET))
  public ModelAndView exportService(){
    System.out.println(patientService.exportService());
    Return new ModelAndView(“dbo/patient/export.jsp”);
  }
}
```
{% endraw %}
