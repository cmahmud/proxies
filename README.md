# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 355
- HTTP: 300 alive / 50 gold
- HTTPS: 187 alive / 13 gold
- SOCKS4: 222 alive / 141 gold
- SOCKS5: 241 alive / 151 gold

## Historical pool

- Discovered: 107131
- Ever alive: 14892
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
