from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
from datetime import datetime
import os
import json
Window.size = (360, 640)
class HealthRecordApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.records = []
        self.data_file = 'health_records.json'
        self.load_records()
    
    def load_records(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.records = json.load(f)
            except:
                self.records = []
    
    def save_records(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.records, f, ensure_ascii=False, indent=2)
    
    def build(self):
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 标题
        title = Label(text='🏥 健康记录助手', size_hint=(1, 0.1), font_size='20sp', bold=True)
        main_layout.add_widget(title)
        
        # 滚动区域
        scroll = ScrollView(size_hint=(1, 0.7))
        self.records_layout = GridLayout(cols=1, size_hint_y=None, padding=10, spacing=10)
        self.records_layout.bind(minimum_height=self.records_layout.setter('height'))
        scroll.add_widget(self.records_layout)
        main_layout.add_widget(scroll)
        
        # 按钮区域
        btn_layout = BoxLayout(size_hint=(1, 0.15), spacing=10)
        
        btn_add = Button(text='➕ 添加记录', background_color=(0.2, 0.6, 0.2, 1), font_size='16sp')
        btn_add.bind(on_press=self.show_add_popup)
        btn_layout.add_widget(btn_add)
        
        btn_view = Button(text='📊 查看历史', background_color=(0.2, 0.4, 0.8, 1), font_size='16sp')
        btn_view.bind(on_press=self.show_history)
        btn_layout.add_widget(btn_view)
        
        main_layout.add_widget(btn_layout)
        
        # 刷新显示
        Clock.schedule_once(lambda dt: self.refresh_display(), 0.5)
        
        return main_layout
    
    def refresh_display(self):
        self.records_layout.clear_widgets()
        if not self.records:
            label = Label(text='暂无记录，点击"添加记录"开始', size_hint_y=None, height=50, color=(0.5, 0.5, 0.5, 1))
            self.records_layout.add_widget(label)
        else:
            # 显示最近 5 条
            for record in self.records[-5:][::-1]:
                card = BoxLayout(orientation='vertical', padding=10, spacing=5, size_hint_y=None, height=100)
                time_label = Label(text=f"⏰ {record.get('time', '未知时间')}", size_hint_y=None, height=30, font_size='14sp', halign='left')
                detail_label = Label(text=f"{record.get('type', '')}: {record.get('value', '')}\n{record.get('note', '')}", size_hint_y=None, height=60, font_size='12sp')
                card.add_widget(time_label)
                card.add_widget(detail_label)
                self.records_layout.add_widget(card)
    
    def show_add_popup(self, instance):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 类型选择
        type_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)
        self.med_btn = Button(text='💊 吃药', background_color=(0.8, 0.6, 0.2, 1))
        self.bp_btn = Button(text='🩸 血压', background_color=(0.8, 0.3, 0.3, 1))
        self.sugar_btn = Button(text='🍬 血糖', background_color=(0.3, 0.6, 0.8, 1))
        
        self.selected_type = '吃药'
        def select_med(*args): self.selected_type = '吃药'; self.med_btn.background_color = (1, 0.8, 0.4, 1); self.bp_btn.background_color = (0.8, 0.3, 0.3, 1); self.sugar_btn.background_color = (0.3, 0.6, 0.8, 1)
        def select_bp(*args): self.selected_type = '血压'; self.med_btn.background_color = (0.8, 0.6, 0.2, 1); self.bp_btn.background_color = (1, 0.5, 0.5, 1); self.sugar_btn.background_color = (0.3, 0.6, 0.8, 1)
        def select_sugar(*args): self.selected_type = '血糖'; self.med_btn.background_color = (0.8, 0.6, 0.2, 1); self.bp_btn.background_color = (0.8, 0.3, 0.3, 1); self.sugar_btn.background_color = (1, 0.7, 0.6, 1)
        
        self.med_btn.bind(on_press=select_med)
        self.bp_btn.bind(on_press=select_bp)
        self.sugar_btn.bind(on_press=select_sugar)
        
        type_layout.add_widget(self.med_btn)
        type_layout.add_widget(self.bp_btn)
        type_layout.add_widget(self.sugar_btn)
        popup_layout.add_widget(type_layout)
        
        # 数值输入
        self.value_input = TextInput(hint_text='输入数值（如：120/80 或 6.5）', multiline=False, size_hint=(1, 0.2), font_size='16sp')
        popup_layout.add_widget(self.value_input)
        
        # 备注
        self.note_input = TextInput(hint_text='备注（可选）', multiline=True, size_hint=(1, 0.3), font_size='14sp')
        popup_layout.add_widget(self.note_input)
        
        # 保存按钮
        save_btn = Button(text='💾 保存记录', background_color=(0.2, 0.8, 0.4, 1), size_hint=(1, 0.2), font_size='16sp')
        save_btn.bind(on_press=lambda x: self.save_record(popup))
        popup_layout.add_widget(save_btn)
        
        self.popup = Popup(title='添加健康记录', content=popup_layout, size_hint=(0.9, 0.7))
        self.popup.open()
    
    def save_record(self, popup):
        value = self.value_input.text.strip()
        note = self.note_input.text.strip()
        if not value:
            return
        
        record = {
            'time': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'type': self.selected_type,
            'value': value,
            'note': note
        }
        self.records.append(record)
        self.save_records()
        self.popup.dismiss()
        self.refresh_display()
        
        # 显示成功提示
        success_popup = Popup(title='✅ 保存成功', content=Label(text='记录已保存！', font_size='18sp'), size_hint=(0.7, 0.3))
        success_popup.open()
        Clock.schedule_once(lambda dt: success_popup.dismiss(), 1.5)
    
    def show_history(self, instance):
        history_layout = ScrollView(size_hint=(1, 1))
        content = BoxLayout(orientation='vertical', padding=20, spacing=10, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        
        if not self.records:
            content.add_widget(Label(text='暂无历史记录', size_hint_y=None, height=50))
        else:
            for i, record in enumerate(self.records[::-1]):
                card = BoxLayout(orientation='vertical', padding=10, spacing=5, size_hint_y=None, height=100)
                card.add_widget(Label(text=f"⏰ {record.get('time', '')}", size_hint_y=None, height=30, halign='left'))
                card.add_widget(Label(text=f"{record.get('type', '')}: {record.get('value', '')}\n{record.get('note', '')}", size_hint_y=None, height=60))
                content.add_widget(card)
        
        close_btn = Button(text='关闭', size_hint=(1, 0.1), height=50)
        close_btn.bind(on_press=lambda x: popup.dismiss())
        content.add_widget(close_btn)
        
        history_layout.add_widget(content)
        popup = Popup(title='📊 历史记录', content=history_layout, size_hint=(0.95, 0.9))
        popup.open()
if __name__ == '__main__':
    HealthRecordApp().run()