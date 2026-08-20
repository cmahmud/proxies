# SyndProxy private pool

## Current pool

- Alive now: 1531
- Gold now: 587
- HTTP: 623 alive / 188 gold
- HTTPS: 401 alive / 92 gold
- SOCKS4: 241 alive / 142 gold
- SOCKS5: 266 alive / 165 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23156
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
