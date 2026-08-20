# SyndProxy private pool

## Current pool

- Alive now: 1423
- Gold now: 585
- HTTP: 562 alive / 190 gold
- HTTPS: 369 alive / 97 gold
- SOCKS4: 224 alive / 137 gold
- SOCKS5: 268 alive / 161 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23132
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
