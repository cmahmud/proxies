# SyndProxy private pool

## Current pool

- Alive now: 1442
- Gold now: 579
- HTTP: 596 alive / 192 gold
- HTTPS: 345 alive / 89 gold
- SOCKS4: 237 alive / 140 gold
- SOCKS5: 264 alive / 158 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23144
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
