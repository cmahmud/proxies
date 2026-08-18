# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 265
- HTTP: 400 alive / 33 gold
- HTTPS: 203 alive / 5 gold
- SOCKS4: 225 alive / 121 gold
- SOCKS5: 240 alive / 106 gold

## Historical pool

- Discovered: 95406
- Ever alive: 11003
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
