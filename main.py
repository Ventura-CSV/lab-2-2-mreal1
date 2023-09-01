def main():
    workhours = (input('45'))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78

   ##################################################
   # Code your program here
   ##################################################
    # overtime = workhours - reg_hours
    # overtime_wage = overtime * ov_rate
    # regular_wage = reg_hours * reg_rate
    # total_wage = regular_wage + overtime_wage
overtime = 45 - 40
overtime_wage = 45 * 27.78
regular_wage = 40 *18.25
total_wage = 18.25 + 27.18



print(f"Regular hours: {40} Regular Charge: {18.25}")
print(f"Overtime hours: {45} Overtime Charge:  {27.78:.2f}")
print(f"Total wage : {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
"return regular_wage, overtime_wage, total_wage"

if __name__ == '__main__':
    main()
