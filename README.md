# SyndProxy private pool

## Current pool

- Alive now: 1323
- Gold now: 384
- HTTP: 470 alive / 94 gold
- HTTPS: 327 alive / 21 gold
- SOCKS4: 218 alive / 125 gold
- SOCKS5: 308 alive / 144 gold

## Historical pool

- Discovered: 134553
- Ever alive: 22122
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
