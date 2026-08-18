# SyndProxy private pool

## Current pool

- Alive now: 1023
- Gold now: 367
- HTTP: 334 alive / 61 gold
- HTTPS: 214 alive / 14 gold
- SOCKS4: 243 alive / 154 gold
- SOCKS5: 232 alive / 138 gold

## Historical pool

- Discovered: 107156
- Ever alive: 15139
- Ever gold: 485

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
