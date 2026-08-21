# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 433
- HTTP: 341 alive / 111 gold
- HTTPS: 234 alive / 35 gold
- SOCKS4: 241 alive / 146 gold
- SOCKS5: 246 alive / 141 gold

## Historical pool

- Discovered: 160279
- Ever alive: 30794
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
