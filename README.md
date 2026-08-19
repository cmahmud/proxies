# SyndProxy private pool

## Current pool

- Alive now: 1311
- Gold now: 389
- HTTP: 462 alive / 94 gold
- HTTPS: 305 alive / 21 gold
- SOCKS4: 236 alive / 131 gold
- SOCKS5: 308 alive / 143 gold

## Historical pool

- Discovered: 134553
- Ever alive: 22101
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
