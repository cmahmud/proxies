# SyndProxy private pool

## Current pool

- Alive now: 755
- Gold now: 265
- HTTP: 214 alive / 30 gold
- HTTPS: 130 alive / 4 gold
- SOCKS4: 204 alive / 120 gold
- SOCKS5: 207 alive / 111 gold

## Historical pool

- Discovered: 99142
- Ever alive: 11881
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
