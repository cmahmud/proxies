# SyndProxy private pool

## Current pool

- Alive now: 1060
- Gold now: 266
- HTTP: 402 alive / 33 gold
- HTTPS: 178 alive / 5 gold
- SOCKS4: 233 alive / 121 gold
- SOCKS5: 247 alive / 107 gold

## Historical pool

- Discovered: 95406
- Ever alive: 11004
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
