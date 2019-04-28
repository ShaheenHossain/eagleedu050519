
from odoo import models, fields, api
import pandas as pd
import os
import numpy


class StudentExamDataSheet(models.Model):
    _name = 'education.exam.results.new'
    _description = "this table contains exam wise student performance Data. ie. attendance,activity etc."

    exam_id = fields.Many2one('education.exam', string='Exam',ondelete="cascade")
    class_id = fields.Many2one('education.class.division', string='Class')
    level_id=fields.Many2one('education.class',string='Level',compute='_get_level',store='True')
    # todo here to change class_id to level
    # todo group for merit list of group
    group=fields.Integer('group')
    division_id = fields.Many2one('education.class.division', string='Division')
    section_id = fields.Many2one('education.class.section', string='Section')
    roll_no = fields.Integer('Roll', related='student_history.roll_no')
    student_id = fields.Many2one('education.student', string='Student')
    student_history=fields.Many2one('education.class.history',"Student History",compute='get_student_history',store="True")
    student_name = fields.Char(string='Student')
    academic_year = fields.Many2one('education.academic.year', string='Academic Year')
    company_id = fields.Many2one('res.company', string='Company',
                                 default=lambda self: self.env['res.company']._company_default_get())
    general_full_mark=fields.Float("Full Mark")
    general_full_mark_converted=fields.Float("Converted Full Mark")
    general_obtained=fields.Integer("General_total")
    general_obtained_converted=fields.Integer("Converted General total")
    general_fail_count = fields.Integer("Genera Fail")
    general_gp=fields.Float('general GP')
    general_gpa = fields.Float("general GPA")

    extra_obtained=fields.Integer("extra Obtained")
    extra_obtained_converted=fields.Integer("Converted Extra Obtained")
    extra_fail_count=fields.Integer("Extra Fail")
    extra_gp=fields.Float('Extra GP')
    extra_gpa = fields.Float("Extra GPA")

    optional_obtained=fields.Integer("Optional obtained")
    optional_obtained_converted=fields.Integer("Converted Optional obtained")
    optional_fail_count=fields.Integer("optional Fail Count")
    optional_gp=fields.Float('Optional LG')
    optional_gpa = fields.Float("Optional GPA")

    net_obtained = fields.Integer(string='Total Marks Scored')
    net_obtained_converted = fields.Integer(string='Total Marks Scored')
    net_pass = fields.Boolean(string='Overall Pass/Fail')
    net_lg=fields.Char("Letter Grade")
    net_gp = fields.Float("Net GP")
    net_gpa=fields.Float("GPA")

    merit_class=fields.Integer("Position In Class")
    merit_section=fields.Integer("Position In section")

    attendance=fields.Integer('Attendance')
    behavior=fields.Many2one("student.behavior","Behavior",default='3')
    sports=fields.Many2one("student.sports","Sports" ,default='3')
    uniform=fields.Many2one("student.uniform","Uniform",default='3')
    cultural=fields.Many2one("student.cultural","Cultural",default='3')
