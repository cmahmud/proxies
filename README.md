# SyndProxy private pool

## Current pool

- Alive now: 919
- Gold now: 273
- HTTP: 382 alive / 31 gold
- HTTPS: 113 alive / 5 gold
- SOCKS4: 217 alive / 130 gold
- SOCKS5: 207 alive / 107 gold

## Historical pool

- Discovered: 99059
- Ever alive: 11269
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
