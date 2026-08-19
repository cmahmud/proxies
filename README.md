# SyndProxy private pool

## Current pool

- Alive now: 1202
- Gold now: 486
- HTTP: 434 alive / 122 gold
- HTTPS: 287 alive / 73 gold
- SOCKS4: 250 alive / 156 gold
- SOCKS5: 231 alive / 135 gold

## Historical pool

- Discovered: 113538
- Ever alive: 16585
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
