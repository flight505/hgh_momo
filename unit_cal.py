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
        total_vol_syringe = st.slider("Total vol syringe (mL)", 0.0, 1.0, 0.1, 0.1)
        total_tick_marks = st.slider("Total tick marks", 1, 100, 1, 1)
        nr_tick_marks_pr_units = st.slider("Nr tick marks pr units", 1, 100, 1, 1)

    def calculate_tick_marks(total_vol_syringe, total_tick_marks, nr_tick_marks_pr_units, mass_hgh):
        draw_to_tick_marks = total_tick_marks / (total_vol_syringe/nr_tick_marks_pr_units) * mass_hgh
        return round(draw_to_tick_marks, 1)

    mass_hgh = calculate_hgh(units_in_vial, units_needed_per_injection, ba_water_added_to_vial)
    rounded_mass_hgh = round(mass_hgh, 4) * 1000

    if st.button("Calculate"):
        st.write("Units needed per injection:", units_needed_per_injection)
        st.write("mass of hgh mg:", rounded_mass_hgh)
        st.write("---")
        st.write("Volume of syringe mL:", total_vol_syringe)
        st.write("💉 Draw upto tick mark:", calculate_tick_marks(total_vol_syringe, total_tick_marks, nr_tick_marks_pr_units, mass_hgh))
        st.write("And you will get swollen!!")
        st.image("https://media.giphy.com/media/gF8FozygvbQJDTm2Ef/giphy.gif")




if __name__ == "__main__":
    main()