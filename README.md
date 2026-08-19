# SyndProxy private pool

## Current pool

- Alive now: 1086
- Gold now: 400
- HTTP: 334 alive / 73 gold
- HTTPS: 246 alive / 12 gold
- SOCKS4: 250 alive / 153 gold
- SOCKS5: 256 alive / 162 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20612
- Ever gold: 869

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
