# Check Hacked Pass Extension (5K or 100K)
================================

This plugin prevents passwords that are found on the top 5K or 100K hacked passwords list. This list was released by Britain’s National Cyber Security Center (NCSC) in collaboration with the Have I Been Pwned website. 
Hacware, Inc. www.hacware.com created this extension to prevent the signin and signup process from allowing end-users from using these passwords.

## Pre Reqs
Pre Reqs - jQuery Validation Plugin - v1.19.1 or later.  
Go to https://jqueryvalidation.org/ or find the entire forked project is here: https://github.com/Hacware-Inc/jquery-validation

There is also a checkHackedPass5K-func.js that is a function and does not require JQuery.

## Getting Started
To Install in HTML webpage, do the following:
```html
<form>
	<input required>
</form>
<script src="jquery.js"></script>
<script src="jquery.validate.js"></script>

<script src="checkHackedPass.js"></script>
OR
<script src="checkHackedPass5K.js"></script>

<script>
    $("form").validate({
          rules: {
            password: {
                required: true,
                CheckPasswordBanned: true
            },

            loginUserName: {
                required: true
            }
        }});
</script>
```
## Product Road Map for 2020
Here are the known issues and improvements that we are planning to address:
* Reduce the size of the checkHackedPass.js (see 5K.js)
* Add NPM installation capabilities
* Create a separate function for other Front End programming languages like React Native
* Create a validator that checks APIs for Hacked Credentials
* Make validator configurable to display a warning vs banning
* Make validator configurable to select top X hacked passwords vs 100K
Thank you for all of the great feedback and our team is planning to release these updates as soon as possible. 

## License
Copyright &copy; Hacware, Inc.<br>
Licensed under the MIT license.

