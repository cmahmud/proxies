# SyndProxy private pool

## Current pool

- Alive now: 829
- Gold now: 385
- HTTP: 216 alive / 79 gold
- HTTPS: 189 alive / 26 gold
- SOCKS4: 213 alive / 148 gold
- SOCKS5: 211 alive / 132 gold

## Historical pool

- Discovered: 163331
- Ever alive: 31863
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
