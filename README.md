# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 281
- HTTP: 362 alive / 32 gold
- HTTPS: 214 alive / 5 gold
- SOCKS4: 225 alive / 134 gold
- SOCKS5: 217 alive / 110 gold

## Historical pool

- Discovered: 99074
- Ever alive: 11398
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
