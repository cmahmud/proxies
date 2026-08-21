# SyndProxy private pool

## Current pool

- Alive now: 1105
- Gold now: 408
- HTTP: 365 alive / 84 gold
- HTTPS: 283 alive / 26 gold
- SOCKS4: 210 alive / 151 gold
- SOCKS5: 247 alive / 147 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29954
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
