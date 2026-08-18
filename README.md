# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 266
- HTTP: 270 alive / 33 gold
- HTTPS: 225 alive / 5 gold
- SOCKS4: 224 alive / 122 gold
- SOCKS5: 250 alive / 106 gold

## Historical pool

- Discovered: 95406
- Ever alive: 11057
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
