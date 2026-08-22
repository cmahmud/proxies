# SyndProxy private pool

## Current pool

- Alive now: 761
- Gold now: 358
- HTTP: 218 alive / 91 gold
- HTTPS: 134 alive / 24 gold
- SOCKS4: 176 alive / 114 gold
- SOCKS5: 233 alive / 129 gold

## Historical pool

- Discovered: 167408
- Ever alive: 32570
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
