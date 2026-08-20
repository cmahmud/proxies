# SyndProxy private pool

## Current pool

- Alive now: 1122
- Gold now: 593
- HTTP: 374 alive / 188 gold
- HTTPS: 305 alive / 101 gold
- SOCKS4: 210 alive / 146 gold
- SOCKS5: 233 alive / 158 gold

## Historical pool

- Discovered: 138957
- Ever alive: 23456
- Ever gold: 921

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
