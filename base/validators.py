from django.core.exceptions import ValidationError

def validateDigits(value):
	if not value.isdigit():
		raise ValidationError('Só aceita números.')

	else:
		return value


def validateNoDigits(value):
	if any(n.isdigit() for n in value):
		raise ValidationError('Este campo não aceita números')

	else:
		return value

def validateNome(value):
    if len(value)<3:
        raise ValidationError('O nome deve possuir três ou mais caracteres')
    
    elif value.isdigit()==True:
        raise ValidationError('O nome não deve possuir números')
    
    else:
        return value

def validateCpf(value):
    if len(value)<11:
        raise ValidationError('Cpf deve possuir 11 caracteres')
    else:
        return value

def validateRg(value):
    if len(value)<7:
        raise ValidationError('O rg deve possuir 7 caracteres')
    else:
        return value

def validateEndereco(value):
    if len(value)<5:
        raise ValidationError('Endereço deve possuir no minimo 5 caracteres')
    else:
        return value

def validateContato(value):
    for i in value:
        if len(i[2:])<9:
            raise('Contato deve possuir 9 caracteres sem o DDD')
        else:
            return value

def validateEmail(value):
    if "@" not in value:
        raise ValidationError('Email Inválido')
    else:
        return value

def validateSenha(value):
    if len(value)<8:
        raise ValidationError('A senha deve possuir 8 caracteres')
    elif len(value)>8:
        raise ValidationError('A senha deve possuir 8 caracteres')

def validateContato(value):
    if len(value[2:])<9:
        raise ValidationError('O contato deve ter 9 digitos sem contar com o DDD')
