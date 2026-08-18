# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 273
- HTTP: 402 alive / 31 gold
- HTTPS: 152 alive / 5 gold
- SOCKS4: 220 alive / 130 gold
- SOCKS5: 202 alive / 107 gold

## Historical pool

- Discovered: 99059
- Ever alive: 11336
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
