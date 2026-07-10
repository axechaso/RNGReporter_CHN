using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace RNGReporter
{
    internal static class GlobalUiFont
    {
        public const string FontFamilyName = "Microsoft YaHei UI";
        private const float DefaultSize = 9F;
        private static readonly HashSet<IntPtr> AppliedForms = new HashSet<IntPtr>();

        public static void Install()
        {
            Application.Idle += ApplyToOpenForms;
        }

        public static Form Prepare(Form form)
        {
            Apply(form);
            return form;
        }

        private static void ApplyToOpenForms(object sender, EventArgs e)
        {
            foreach (Form form in Application.OpenForms)
            {
                if (form.IsDisposed || AppliedForms.Contains(form.Handle))
                    continue;

                Apply(form);
                AppliedForms.Add(form.Handle);
            }
        }

        private static void Apply(Control control)
        {
            ApplyControlFont(control);

            var grid = control as DataGridView;
            if (grid != null)
                ApplyGridFont(grid);

            var toolStrip = control as ToolStrip;
            if (toolStrip != null)
                ApplyToolStripFont(toolStrip);

            if (control.ContextMenuStrip != null)
                ApplyToolStripFont(control.ContextMenuStrip);

            foreach (Control child in control.Controls)
            {
                Apply(child);
            }
        }

        private static void ApplyControlFont(Control control)
        {
            control.Font = CreateUiFont(control.Font);
        }

        private static void ApplyGridFont(DataGridView grid)
        {
            grid.Font = CreateUiFont(grid.Font);
            ApplyCellStyleFont(grid.DefaultCellStyle, grid.Font);
            ApplyCellStyleFont(grid.AlternatingRowsDefaultCellStyle, grid.Font);
            ApplyCellStyleFont(grid.ColumnHeadersDefaultCellStyle, grid.Font);
            ApplyCellStyleFont(grid.RowHeadersDefaultCellStyle, grid.Font);
            ApplyCellStyleFont(grid.RowsDefaultCellStyle, grid.Font);

            foreach (DataGridViewColumn column in grid.Columns)
            {
                ApplyCellStyleFont(column.DefaultCellStyle, grid.Font);
            }
        }

        private static void ApplyCellStyleFont(DataGridViewCellStyle style, Font fallback)
        {
            style.Font = CreateUiFont(style.Font ?? fallback);
        }

        private static void ApplyToolStripFont(ToolStrip toolStrip)
        {
            toolStrip.Font = CreateUiFont(toolStrip.Font);

            foreach (ToolStripItem item in toolStrip.Items)
            {
                ApplyToolStripItemFont(item);
            }
        }

        private static void ApplyToolStripItemFont(ToolStripItem item)
        {
            item.Font = CreateUiFont(item.Font);

            var menuItem = item as ToolStripMenuItem;
            if (menuItem == null)
                return;

            foreach (ToolStripItem child in menuItem.DropDownItems)
            {
                ApplyToolStripItemFont(child);
            }
        }

        private static Font CreateUiFont(Font source)
        {
            float size = source == null ? DefaultSize : source.Size;
            FontStyle style = source == null ? FontStyle.Regular : source.Style;
            GraphicsUnit unit = source == null ? GraphicsUnit.Point : source.Unit;

            if (source != null && source.FontFamily.Name == FontFamilyName)
                return source;

            return new Font(FontFamilyName, size, style, unit, 134);
        }
    }
}
