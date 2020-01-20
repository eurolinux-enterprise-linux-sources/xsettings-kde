
Summary: XSettings Daemon for KDE
Name:    xsettings-kde
Version: 0.12.3
Release: 5%{?dist}
License: GPLv2+
Group:   User Interface/Desktops 
Source0: http://distro.ibiblio.org/pub/linux/distributions/mageia/software/xsettings-kde/%{version}/xsettings-kde-%{version}.tar.bz2 
URL:     http://svnweb.mageia.org/soft/theme/xsettings-kde/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# fedora doesn't use ~/.kde4 like mandriva
Patch1: xsettings-kde-0.9-kde4.patch
# rewrite Net/ThemeName handling: set it based on .gtkrc-2.0-kde4 (kcm-gtk)
# This makes sure GTK+ 3 also picks up the theme setting from kcm-gtk.
# TODO: Discuss with upstream.
Patch2: xsettings-kde-0.12.3-gtktheme.patch

## upstreamable patches
# drop needless spinloop introduced in https://bugzilla.redhat.com/727822
Patch50: xsettings-kde-wakeups.patch

Source10: xsettings-kde.desktop

BuildRequires: glib2-devel
BuildRequires: libX11-devel

%description
This package provides a XSettings daemon for KDE Desktop Environment.
It allows XSettings aware applications (all GTK+ 2 and GNOME 2 applications)
to be informed instantly of changes in KDE configuration, such as theme name,
default font and so on.


%prep
%setup -q

%patch1 -p1 -b .kde4
%patch2 -p1 -b .gtktheme
%patch50 -p1 -b .wakeups


%build

make %{?_smp_mflags} CFLAGS="%{optflags}" lib=%{_lib}


%install
rm -rf %{buildroot}

install -p -m755 -D  xsettings-kde %{buildroot}%{_bindir}/xsettings-kde

install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{_datadir}/autostart/xsettings-kde.desktop


%clean
rm -rf %{buildroot}


%files 
%defattr(-,root,root,-)
%doc ChangeLog README COPYING
%{_bindir}/*
%{_datadir}/autostart/*


%changelog
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Rex Dieter <rdieter@fedoraproject.org> 0.12.3-3
- drop some needless wakeups introduced with Gtk/IMModule support

* Thu Mar 08 2012 Rex Dieter <rdieter@fedoraproject.org> 0.12.3-2.1
- rebuild (for f16/kde48)

* Wed Jan 18 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.12.3-2
- fix use-after-free bug in my patch

* Tue Jan 17 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.12.3-1
- update to 0.12.3
- drop upstreamed immodule patch
- rewrite Net/ThemeName handling: set it based on .gtkrc-2.0-kde4 (kcm-gtk)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 22 2011 Rex Dieter <rdieter@fedoraproject.org> 0.12.2-2
- RFE: Gtk/IMModule support (#727822)

* Sat Aug 06 2011 Rex Dieter <rdieter@fedoraproject.org> 0.12.2-1
- 0.12.2

* Thu Mar 17 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.12-4
- update upstream URL (viewvc -> svnweb)

* Mon Mar 14 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.12-3
- add support for Gtk/CursorThemeName (#591746)
- drop SVN checkout script, we have a tarball now

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Rex Dieter <rdieter@fedoraproject.org> 0.12-1
- 0.12

* Mon Nov 29 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.11-3
- fix the gtk-menu-images patch to set the setting BEFORE notifying apps

* Mon Nov 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.11-2
- make GTK+ apps display menu images in KDE

* Sat Aug 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.11-1
- xsettings-0.11

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.10-1
- xsettings-0.10

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 30 2008 Rex Dieter <rdieter@fedoraproject.org> 0.9-1
- resurrect latest kde4-enabled version, yay.

* Sun Jan 27 2008 Manuel Wolfshant <wolfy@fedoraproject.org> 0.6-3
- small fixes

* Sun Dec 30 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.6-2
- fedora-ize

* Wed Sep 26 2007 Frederic Crozat <fcrozat@mandriva.com> 0.6-1mdv2008.0
+ Revision: 93073
- Release 0.6 :
 -failover correctly when some configuration files aren't present

* Fri Sep 21 2007 Frederic Crozat <fcrozat@mandriva.com> 0.5-1mdv2008.0
+ Revision: 91946
- Release 0.5
 - handle multiple kde profiles specified as prefixes

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.com> 0.4-2mdv2008.0
+ Revision: 76611
- rebuild for 2008
- don't package COPYING
- Import xsettings-kde

* Wed Sep 13 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4-1mdv2007.0
- Release 0.4 :
 * change theme according to color scheme for Ia Ora (Mdv bug #25574)
 * fix theme detection
 * support kde profile
 * don't change theme if ~/.gtkrc-2.0 exists

* Mon Mar 06 2006 Frederic Crozat <fcrozat@mandriva.com> 0.3-1mdk
- Release 0.3 :
 - support Net/FallbackIconTheme, fix Mdk bug #19441)

* Thu Aug 25 2005 Frederic Crozat <fcrozat@mandriva.com> 0.2-1mdk 
- Release 0.2 :
 - force gnome-vfs gtk2 file selector backend

* Wed Jul 27 2005 Frederic Crozat <fcrozat@mandriva.com> 0.1-1mdk 
- Initial package
