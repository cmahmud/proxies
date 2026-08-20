# SyndProxy private pool

## Current pool

- Alive now: 1583
- Gold now: 651
- HTTP: 607 alive / 217 gold
- HTTPS: 492 alive / 110 gold
- SOCKS4: 233 alive / 157 gold
- SOCKS5: 251 alive / 167 gold

## Historical pool

- Discovered: 141223
- Ever alive: 23966
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
