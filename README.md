# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 363
- HTTP: 207 alive / 72 gold
- HTTPS: 240 alive / 16 gold
- SOCKS4: 209 alive / 135 gold
- SOCKS5: 200 alive / 140 gold

## Historical pool

- Discovered: 149418
- Ever alive: 26533
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
