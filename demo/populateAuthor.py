import os
import django


def populate():
    p = add_plan('b1', 'b1', 10, 100.00, 'USD')
    print("Added Object Plan : ", p)

    p = add_plan('b2', 'b2', 10, 200.00, 'USD')
    print("Added Object Plan : ", p)

    p = add_plan('b3', 'b3', 10, 300.00, 'USD')
    print("Added Object Plan : ", p)


def add_plan(label, description, no_of_users, monthly_charges, currency):
    p = Plan.objects.get_or_create(label=label, description=description,
                                   no_of_users=no_of_users, monthly_charges=monthly_charges, currency=currency)[0]
    return p


# Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    django.setup()
    from contrib.plan.models import Plan
    populate()
