# SyndProxy private pool

## Current pool

- Alive now: 1417
- Gold now: 581
- HTTP: 565 alive / 190 gold
- HTTPS: 369 alive / 96 gold
- SOCKS4: 223 alive / 137 gold
- SOCKS5: 260 alive / 158 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23133
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
