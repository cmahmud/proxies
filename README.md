# SyndProxy private pool

## Current pool

- Alive now: 1671
- Gold now: 613
- HTTP: 625 alive / 216 gold
- HTTPS: 469 alive / 114 gold
- SOCKS4: 221 alive / 134 gold
- SOCKS5: 356 alive / 149 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23919
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
