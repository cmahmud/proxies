# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 338
- HTTP: 231 alive / 91 gold
- HTTPS: 172 alive / 19 gold
- SOCKS4: 187 alive / 129 gold
- SOCKS5: 193 alive / 99 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28947
- Ever gold: 1116

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
