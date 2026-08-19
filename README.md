# SyndProxy private pool

## Current pool

- Alive now: 1296
- Gold now: 528
- HTTP: 489 alive / 185 gold
- HTTPS: 345 alive / 57 gold
- SOCKS4: 217 alive / 123 gold
- SOCKS5: 245 alive / 163 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19656
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
