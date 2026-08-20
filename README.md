# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 403
- HTTP: 279 alive / 90 gold
- HTTPS: 190 alive / 23 gold
- SOCKS4: 208 alive / 135 gold
- SOCKS5: 214 alive / 155 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27612
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
