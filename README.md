# SyndProxy private pool

## Current pool

- Alive now: 1556
- Gold now: 580
- HTTP: 570 alive / 196 gold
- HTTPS: 400 alive / 99 gold
- SOCKS4: 228 alive / 149 gold
- SOCKS5: 358 alive / 136 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23650
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
