
#%%
import groups
by_category, category_strs=groups.get_category_random(myparser.all_summary, myparser.all_emails, category)

tiny_groups = [group for group in by_category if len(group)<3]
tiny_groups_strs = [category_strs[by_category.index(group)] for group in by_category if len(group)<=2]
big_groups_strs = [category_val for category_val in category_strs if category_val not in tiny_groups_strs]

print("")
print("big groups: "+str(big_groups_strs))

for tiny_group_idx, tiny_group in enumerate(tiny_groups):
    add_to = input("Add tiny group "+str(tiny_groups_strs[tiny_group_idx])+" to which big group? ")
    while add_to not in big_groups_strs:
        add_to = input("Not a big group. Add tiny group "+str(tiny_groups_strs[tiny_group_idx])+" to which big group? ")
    by_category[category_strs.index(add_to)]=by_category[category_strs.index(add_to)]+tiny_group
    