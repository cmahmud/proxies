# SyndProxy private pool

## Current pool

- Alive now: 825
- Gold now: 360
- HTTP: 269 alive / 100 gold
- HTTPS: 161 alive / 23 gold
- SOCKS4: 195 alive / 131 gold
- SOCKS5: 200 alive / 106 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28955
- Ever gold: 1117

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
