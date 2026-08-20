# SyndProxy private pool

## Current pool

- Alive now: 705
- Gold now: 379
- HTTP: 179 alive / 72 gold
- HTTPS: 134 alive / 20 gold
- SOCKS4: 198 alive / 146 gold
- SOCKS5: 194 alive / 141 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26360
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
