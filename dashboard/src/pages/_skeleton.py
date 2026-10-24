from __future__ import annotations

import streamlit as st


def planned_page(title: str, items: list[str]) -> None:
    st.header(title)
    st.info(
        "Halaman ini belum diimplementasikan. Kerangka navigasi sudah tersedia "
        "dan akan diisi pada Phase 2B. Tidak ada analisis atau angka yang "
        "ditampilkan sebelum diimplementasikan."
    )
    st.markdown("**Rencana isi (Phase 2B):**")
    for item in items:
        st.markdown(f"- {item}")
