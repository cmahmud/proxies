# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 246
- HTTP: 443 alive / 32 gold
- HTTPS: 176 alive / 7 gold
- SOCKS4: 221 alive / 113 gold
- SOCKS5: 225 alive / 94 gold

## Historical pool

- Discovered: 91719
- Ever alive: 9079
- Ever gold: 361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
