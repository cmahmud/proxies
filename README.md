# SyndProxy private pool

## Current pool

- Alive now: 837
- Gold now: 410
- HTTP: 230 alive / 89 gold
- HTTPS: 156 alive / 25 gold
- SOCKS4: 211 alive / 146 gold
- SOCKS5: 240 alive / 150 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29122
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
