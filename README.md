# SyndProxy private pool

## Current pool

- Alive now: 1067
- Gold now: 261
- HTTP: 430 alive / 30 gold
- HTTPS: 181 alive / 4 gold
- SOCKS4: 221 alive / 120 gold
- SOCKS5: 235 alive / 107 gold

## Historical pool

- Discovered: 95406
- Ever alive: 11001
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
