{
  'targets': [
    {
      'target_name': 'node_sqlite3',
      'sources': [
        'src/database.cc',
        'src/node_sqlite3.cc',
        'src/statement.cc'
      ],
      'dependencies': [
        'deps/sqlite3/binding.gyp:sqlite3'
      ],
      'conditions': [       
        [ 'OS=="win"', {
          'defines': [
            'PLATFORM="win32"',
            '_WINDOWS',
            '__WINDOWS__', # ltdl
            'BUILDING_NODE_EXTENSION'
          ],
          'libraries': [ 
              '<@(node_root_dir)\\$(Configuration)\\lib\\zlib.lib',
              '<@(node_root_dir)\\$(Configuration)\\lib\\libuv.lib',
              '<@(node_root_dir)\\$(Configuration)\\lib\\http_parser.lib',
              '<@(node_root_dir)\\$(Configuration)\\lib\\cares.lib',
              '<@(node_root_dir)\\build\\$(Configuration)\\lib\\v8_base.lib',
              '<@(node_root_dir)\\build\\$(Configuration)\\lib\\v8_nosnapshot.lib',
              '<@(node_root_dir)\\winrtlibs\\ws2_32.lib',
              '<@(node_root_dir)\\winrtlibs\\winmm.lib',
              '<@(node_root_dir)\\winrtlibs\\psapi.lib',
              '<@(node_root_dir)\\winrtlibs\\IPHLPAPI.lib',
              '<@(node_root_dir)\\winrtlibs\\advapi32.lib'
          ]
          }
        ], # windows
      ] # condition
    }
  ]
}
