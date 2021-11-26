import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-web",
    description="Meta package for oca-web Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-web_action_conditionable',
        'odoo12-addon-web_advanced_filter',
        'odoo12-addon-web_advanced_search',
        'odoo12-addon-web_advanced_search_wildcard',
        'odoo12-addon-web_calendar_slot_duration',
        'odoo12-addon-web_company_color',
        'odoo12-addon-web_dashboard_tile',
        'odoo12-addon-web_decimal_numpad_dot',
        'odoo12-addon-web_dialog_size',
        'odoo12-addon-web_disable_browser_autocomplete',
        'odoo12-addon-web_disable_export_group',
        'odoo12-addon-web_domain_field',
        'odoo12-addon-web_domain_field_example',
        'odoo12-addon-web_drop_target',
        'odoo12-addon-web_edit_user_filter',
        'odoo12-addon-web_editor_background_color',
        'odoo12-addon-web_environment_ribbon',
        'odoo12-addon-web_export_view',
        'odoo12-addon-web_favicon',
        'odoo12-addon-web_group_by_percentage',
        'odoo12-addon-web_group_expand',
        'odoo12-addon-web_ir_actions_act_multi',
        'odoo12-addon-web_ir_actions_act_view_reload',
        'odoo12-addon-web_ir_actions_act_window_message',
        'odoo12-addon-web_ir_actions_close_wizard_refresh_view',
        'odoo12-addon-web_listview_range_select',
        'odoo12-addon-web_m2x_options',
        'odoo12-addon-web_no_bubble',
        'odoo12-addon-web_no_crawler',
        'odoo12-addon-web_notify',
        'odoo12-addon-web_pivot_computed_measure',
        'odoo12-addon-web_pwa_oca',
        'odoo12-addon-web_refresher',
        'odoo12-addon-web_responsive',
        'odoo12-addon-web_responsive_company',
        'odoo12-addon-web_search_with_and',
        'odoo12-addon-web_searchbar_full_width',
        'odoo12-addon-web_send_message_popup',
        'odoo12-addon-web_set_single_page_hidden',
        'odoo12-addon-web_sheet_full_width',
        'odoo12-addon-web_switch_context_warning',
        'odoo12-addon-web_timeline',
        'odoo12-addon-web_translate_dialog',
        'odoo12-addon-web_tree_duplicate',
        'odoo12-addon-web_tree_dynamic_colored_field',
        'odoo12-addon-web_tree_image_tooltip',
        'odoo12-addon-web_tree_many2one_clickable',
        'odoo12-addon-web_tree_resize_column',
        'odoo12-addon-web_view_calendar_column',
        'odoo12-addon-web_view_calendar_list',
        'odoo12-addon-web_view_searchpanel',
        'odoo12-addon-web_widget_bokeh_chart',
        'odoo12-addon-web_widget_child_selector',
        'odoo12-addon-web_widget_color',
        'odoo12-addon-web_widget_datepicker_fulloptions',
        'odoo12-addon-web_widget_digitized_signature',
        'odoo12-addon-web_widget_domain_editor_dialog',
        'odoo12-addon-web_widget_dropdown_dynamic',
        'odoo12-addon-web_widget_dropdown_dynamic_example',
        'odoo12-addon-web_widget_float_formula',
        'odoo12-addon-web_widget_image_download',
        'odoo12-addon-web_widget_image_url',
        'odoo12-addon-web_widget_image_webcam',
        'odoo12-addon-web_widget_json_graph',
        'odoo12-addon-web_widget_many2many_tags_multi_selection',
        'odoo12-addon-web_widget_mermaid',
        'odoo12-addon-web_widget_model_viewer',
        'odoo12-addon-web_widget_mpld3_chart',
        'odoo12-addon-web_widget_numeric_step',
        'odoo12-addon-web_widget_one2many_product_picker',
        'odoo12-addon-web_widget_one2many_product_picker_sale_stock',
        'odoo12-addon-web_widget_one2many_product_picker_sale_stock_available_info_popup',
        'odoo12-addon-web_widget_open_tab',
        'odoo12-addon-web_widget_plotly_chart',
        'odoo12-addon-web_widget_timepicker',
        'odoo12-addon-web_widget_url_advanced',
        'odoo12-addon-web_widget_url_translatable',
        'odoo12-addon-web_widget_x2many_2d_matrix',
        'odoo12-addon-web_widget_x2many_2d_matrix_example',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
