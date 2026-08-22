# SyndProxy private pool

## Current pool

- Alive now: 977
- Gold now: 393
- HTTP: 352 alive / 86 gold
- HTTPS: 166 alive / 26 gold
- SOCKS4: 213 alive / 146 gold
- SOCKS5: 246 alive / 135 gold

## Historical pool

- Discovered: 167116
- Ever alive: 32528
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
