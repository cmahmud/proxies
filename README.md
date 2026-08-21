# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 419
- HTTP: 259 alive / 92 gold
- HTTPS: 173 alive / 25 gold
- SOCKS4: 215 alive / 140 gold
- SOCKS5: 263 alive / 162 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29035
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
