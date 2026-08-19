# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 394
- HTTP: 316 alive / 72 gold
- HTTPS: 225 alive / 15 gold
- SOCKS4: 257 alive / 147 gold
- SOCKS5: 237 alive / 160 gold

## Historical pool

- Discovered: 129319
- Ever alive: 20475
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
