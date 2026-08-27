# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 429
- HTTP: 118 alive / 79 gold
- HTTPS: 124 alive / 22 gold
- SOCKS4: 180 alive / 159 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42169
- Ever gold: 1352

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
