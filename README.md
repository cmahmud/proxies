# SyndProxy private pool

## Current pool

- Alive now: 1195
- Gold now: 532
- HTTP: 438 alive / 182 gold
- HTTPS: 331 alive / 83 gold
- SOCKS4: 219 alive / 127 gold
- SOCKS5: 207 alive / 140 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19779
- Ever gold: 797

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
