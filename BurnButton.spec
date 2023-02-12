# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['src/main/python/Main.py'],
             pathex=[],
             binaries=[],
             datas=[('src/main/python/resources', 'resources')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='BurnButton',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='src/main/icons/Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='BurnButton')
app = BUNDLE(coll,
             name='BurnButton.app',
             icon='src/main/icons/icons.icns',
             bundle_identifier=None)
