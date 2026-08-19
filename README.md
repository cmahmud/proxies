# SyndProxy private pool

## Current pool

- Alive now: 1268
- Gold now: 389
- HTTP: 449 alive / 94 gold
- HTTPS: 284 alive / 21 gold
- SOCKS4: 225 alive / 131 gold
- SOCKS5: 310 alive / 143 gold

## Historical pool

- Discovered: 134553
- Ever alive: 22082
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
