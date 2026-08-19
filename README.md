# SyndProxy private pool

## Current pool

- Alive now: 1201
- Gold now: 533
- HTTP: 441 alive / 183 gold
- HTTPS: 334 alive / 83 gold
- SOCKS4: 218 alive / 127 gold
- SOCKS5: 208 alive / 140 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19779
- Ever gold: 797

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
