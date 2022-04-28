import streamlit as st


def main():



    st.set_page_config(page_title="Config")

    st.title("💉hgh calculator for Momo - he cant be bothered with this")




    with st.sidebar:
            units_needed_per_injection = st.slider("Units in injection (IU)", 0, 20, 2, 1)
            units_in_vial = st.slider("Units in vial (IU)", 0, 100, 72, 1)
            ba_water_added_to_vial = st.slider("BA water added to vial (mL)", 0.1, 10.0, 2.0, 0.05)

    def calculate_hgh(units_in_vial, units_needed_per_injection, ba_water_added_to_vial):
        hgh = (ba_water_added_to_vial * units_needed_per_injection) / units_in_vial
        return hgh

    with st.sidebar:
        st.write("---")
        total_vol_syringe = st.slider("Total vol syringe (mL)", 0.0, 1.0, 0.3, 0.1)
        total_tick_marks = st.slider("Total tick marks", 1, 100, 30, 1)
        nr_tick_marks_pr_units = st.slider("Nr tick marks pr units", 1, 100, 1, 1)

    def calculate_tick_marks(total_vol_syringe, total_tick_marks, nr_tick_marks_pr_units, mass_hgh):
        draw_to_tick_marks = total_tick_marks / (total_vol_syringe/nr_tick_marks_pr_units) * mass_hgh
        return draw_to_tick_marks

    mass_hgh = calculate_hgh(units_in_vial, units_needed_per_injection, ba_water_added_to_vial)
    rounded_mass_hgh = round(((mass_hgh) * 1000),2)

    if st.button("Calculate"):
        st.write("Units needed per injection:", units_needed_per_injection)
        st.write("---")
        st.write("💉 Draw upto tick mark:", round(calculate_tick_marks(total_vol_syringe, total_tick_marks, nr_tick_marks_pr_units, mass_hgh),2))
        st.write("mass of hgh mcg:", rounded_mass_hgh)
        st.write("Get UltraSwole!!")
        st.image("https://media.giphy.com/media/f8VSLphYUBCCxn09tD/giphy.gif", width=300)




if __name__ == "__main__":
    main()