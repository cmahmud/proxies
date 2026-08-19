# SyndProxy private pool

## Current pool

- Alive now: 1276
- Gold now: 372
- HTTP: 408 alive / 86 gold
- HTTPS: 266 alive / 16 gold
- SOCKS4: 258 alive / 134 gold
- SOCKS5: 344 alive / 136 gold

## Historical pool

- Discovered: 133937
- Ever alive: 21471
- Ever gold: 881

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
