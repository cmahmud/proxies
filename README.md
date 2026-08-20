# SyndProxy private pool

## Current pool

- Alive now: 835
- Gold now: 366
- HTTP: 211 alive / 74 gold
- HTTPS: 201 alive / 16 gold
- SOCKS4: 215 alive / 136 gold
- SOCKS5: 208 alive / 140 gold

## Historical pool

- Discovered: 149418
- Ever alive: 26539
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
