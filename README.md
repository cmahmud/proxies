# SyndProxy private pool

## Current pool

- Alive now: 768
- Gold now: 265
- HTTP: 219 alive / 30 gold
- HTTPS: 129 alive / 4 gold
- SOCKS4: 205 alive / 120 gold
- SOCKS5: 215 alive / 111 gold

## Historical pool

- Discovered: 99142
- Ever alive: 11888
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
