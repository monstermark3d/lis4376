#
# Functions debugged by Mark Trombly
#
def get_requirements():
    print("Payroll Calculator")
    print("\nProgram Requirements:\n"
          + "1. Must use float data type for user input.\n"
          + "2. Overtime rate: 1.5 times hourly rate (hours over 40).\n"
          + "3. Holiday rate: 2.0 times hourly rate (all holiday hours).\n"
          + "4. Must format currency with dollar sign, and round to two decimal places.\n"
          + "5. Create at least three functions that are called by the program:\n"
          + "\ta. main(): calls at least two other functions.\n"
          + "\tb. get_requirements(): displays the program requirements.\n"
          + "\tc. calculate_payroll(): calculates an individuals one-week paycheck.\n")


def calculate_payroll():
    # constants to represent base hours, overtime and holiday rates
    # Note: python doesn't provide true constants
    BASE_HOURS = 40     # base hours
    OT_RATE = 1.5       # overtime rate
    HOLIDAY_RATE = 2.0  # holiday rate

    # IPO: Input > Process > Output
    # Get user data
    print("Input:")
    # Get hours worked and hourly pay rate
    hours = float(input('Enter hours worked: '))
    holiday_hours = float(input('Enter holiday hours: '))
    pay_rate = float(input('Enter hourly pay rate: '))

    # Process:
    # Calculations
    base_pay = BASE_HOURS * pay_rate    # fix base pay -> base_pay = BASE_HOURS - pay_rate
    
    # add validation for hours > BASE_HOURS for overtime calculation
    if hours > BASE_HOURS:  # validate overtime hours if greater than BASE_HOURS
        overtime_hours = hours - BASE_HOURS # calculate overtime hours from BASE_HOURS
    else:
        overtime_hours = 0.0    # else set overtime_hours to 0.0

    # Calculate and Display gross pay
    if hours > BASE_HOURS:  # if hours are more than BASE_HOURS then overtime exists
        # Calculate gross pay with overtime

        # Calculate overtime pay
        overtime_pay = overtime_hours * pay_rate * OT_RATE

        # Calculate holiday pay
        holiday_pay = holiday_hours * pay_rate * HOLIDAY_RATE

        # Calculate gross pay
        gross_pay = BASE_HOURS * pay_rate + overtime_pay + holiday_pay
        print_pay(base_pay, overtime_pay, holiday_pay, gross_pay)
    else:
        # Calculate gross pay without overtime, but include holiday pay
        overtime_pay = 0
        holiday_pay = holiday_hours * pay_rate * HOLIDAY_RATE
        gross_pay = hours * pay_rate + holiday_pay

        # Display pay
        print_pay(base_pay, overtime_pay, holiday_pay, gross_pay) # fix funciton argument names -> print_pay(b_pay, o_pay, h_pay, g_pay)

        print()


def print_pay(base_pay, overtime_pay, holiday_pay, gross_pay):
    print("\nOutput:")                                              # add indention
    print("{0:<10} ${1:,.2f}".format('Base:', base_pay))            # add indention
    print("{0:<10} ${1:,.2f}".format('Overtime:', overtime_pay))    # add indention
    print("{0:<10} ${1:,.2f}".format('Holiday:', holiday_pay))      # add indention
    print("{0:<10} ${1:,.2f}".format('Gross:', gross_pay))          # add indention
