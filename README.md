# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 431
- HTTP: 341 alive / 111 gold
- HTTPS: 222 alive / 35 gold
- SOCKS4: 248 alive / 145 gold
- SOCKS5: 248 alive / 140 gold

## Historical pool

- Discovered: 160279
- Ever alive: 30793
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
