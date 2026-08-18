# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 348
- HTTP: 265 alive / 50 gold
- HTTPS: 185 alive / 15 gold
- SOCKS4: 221 alive / 134 gold
- SOCKS5: 217 alive / 149 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14923
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
