# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from pootle_app.models import Directory

from .models import VirtualFolderTreeItem


def make_vfolder_treeitem_dict(vfolder_treeitem):
    return {
        'href_all': vfolder_treeitem.get_translate_url(),
        'href_todo': vfolder_treeitem.get_translate_url(
            state='incomplete'),
        'href_sugg': vfolder_treeitem.get_translate_url(
            state='suggestions'),
        'href_critical': vfolder_treeitem.get_critical_url(),
        'title': vfolder_treeitem.vfolder.name,
        'code': vfolder_treeitem.code,
        'priority': vfolder_treeitem.vfolder.priority,
        'is_grayed': not vfolder_treeitem.is_visible,
        'stats': vfolder_treeitem.get_stats(
            include_children=False),
        'icon': 'vfolder'}


def vftis_for_child_dirs(directory):
    """
    Returns the vfoldertreeitems for a directory's child directories
    """
    child_dir_pks = [
        child.pk
        for child
        in directory.children
        if isinstance(child, Directory)]
    return VirtualFolderTreeItem.objects.filter(
        directory__pk__in=child_dir_pks)
