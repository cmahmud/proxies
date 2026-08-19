# SyndProxy private pool

## Current pool

- Alive now: 905
- Gold now: 326
- HTTP: 295 alive / 60 gold
- HTTPS: 163 alive / 15 gold
- SOCKS4: 207 alive / 125 gold
- SOCKS5: 240 alive / 126 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20102
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
