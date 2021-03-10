from django.db import models
from datetime import datetime, timedelta


class Alias(models.Model):
	"""The class used to describe model Alias."""

	alias = models.CharField(max_length=24)
	target = models.CharField(max_length=24)
	start = models.DateTimeField()
	end = models.DateTimeField(null=True)

	def __str__(self):
		return self.alias, self.target, self.start, self.end

def create_an_alias(alias, target, start, end=None):
	"""The function used to create new alias."""

	if not Alias.objects.filter(target=target):            # We don't have this target in our db. 
														   # But we need to check we had this alias before. 
		if Alias.objects.filter(alias=alias):
			print("New alias can't create. This alias was already used for other target.")
			return
		else:
			our_alias = Alias(alias=alias, target=target, start=start, end=end if end == None else end - timedelta(microseconds=1))
			our_alias.save()
			print("New alias was created")
			return our_alias
	
	else:
		
		if not Alias.objects.filter(alias=alias, target=target):    # We have this target, but don't have this new alias.
			if Alias.objects.filter(alias=alias):
				print("New alias can't create. This alias was already used for other target.")
				return
			else:

				our_alias = Alias(alias, target, start, end - timedelta(microseconds=1))
				our_alias.save()
				print("New alias was created")
				return our_alias
		
		else:      # We have this target and this alias already. Now we need to check time limit.
			all_aliases = Alias.objects.filter(alias=alias, target=target)
			
			for al in all_aliases:    # We check all aliases for 'end' argument. If it's special case or not.
				if al.end == None:    # It's a special case.   
					if end == None:
						print("New alias can't create. Use other time limit.")
						return
					
					elif end > al.start:
						print("New alias can't create. Use other time limit.")
						return 
				else:                # It's not a special case.
					if al.start > end or al.end < start:
						continue
					else: 
						print("New alias can't create. Use other time limit.")
						return

			
			our_alias = Alias(
				alias=alias, 
				target=target, 
				start=start, 
				end=end - timedelta(microseconds=1)
				)

			our_alias.save()
			print("New alias was created")
			return our_alias

	                               


def get_aliases(target, start, end): 
	"""The function used to get Aliases."""

	aliases = Alias.objects.filter(target=target)
	result = {}
	
	if not aliases:
		print("Alias was not found")
		return {}
	
	if end == None:
		for al in aliases:
			if al.end == None:
				if start < al.start:
					try:
						result[al.alias] += ((al.start, al.end),)
					except KeyError:
						result[al.alias] = ((al.start, al.end),)
			elif start < al.end:
				try:
					result[al.alias] += ((al.start, al.end),)
				except KeyError:
					result[al.alias] = ((al.start, al.end),)
	else:
		for al in aliases:
			
			if al.end == None:
				if al.start < end:
					try:
						result[al.alias] += ((al.start, al.end),)
					except KeyError:
						result[al.alias] = ((al.start, al.end),)
			
			elif (start < al.end) or (end > al.start):
				try:
					result[str(al.alias)] += ((al.start, al.end),)
				except KeyError:
					result[str(al.alias)] = ((al.start, al.end),)
	return result


def alias_replace(existing_alias, replace_at, new_alias_value):
	"""The function used to replace Aliases."""

	old_alias = Alias.objects.filter(alias=existing_alias)
	
	if not old_alias:
		print("Nothing to replace. Use other alias.")
		return

	target = list(old_alias)[0].target

	old_alias.delete()

	new_alias = create_an_alias(
		alias=new_alias_value, 
		target=target, 
		start=replace_at, 
		end=None
		)

	return new_alias.alias

