# SyndProxy private pool

## Current pool

- Alive now: 1311
- Gold now: 373
- HTTP: 426 alive / 86 gold
- HTTPS: 272 alive / 17 gold
- SOCKS4: 264 alive / 134 gold
- SOCKS5: 349 alive / 136 gold

## Historical pool

- Discovered: 133937
- Ever alive: 21466
- Ever gold: 881

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
