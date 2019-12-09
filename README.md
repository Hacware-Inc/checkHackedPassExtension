# Check Hacked Pass Extenstion
================================

This plugin prevents passwords that are founded on the top 100K hacked passwords list. This list was released by Britain’s National Cyber Security Center (NCSC) in collaboration with the Have I Been Pwned website. 
Hacware, Inc. www.hacware.com created this extension to prevent the signin and signup process from allowing end-users from using these passwords.

## Pre Reqs
Pre Reqs - jQuery Validation Plugin - v1.19.1 or later.  
Go to https://jqueryvalidation.org/ or find the entire forked project is here: https://github.com/Hacware-Inc/jquery-validation

## Getting Started
To Install in HTML webpage, do the following:
```html
<form>
	<input required>
</form>
<script src="jquery.js"></script>
<script src="jquery.validate.js"></script>
<script src="checkHackedPass.js"></script>

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
## License
Copyright &copy; Hacware, Inc.<br>
Licensed under the MIT license.
