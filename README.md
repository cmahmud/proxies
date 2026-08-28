# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 431
- HTTP: 116 alive / 79 gold
- HTTPS: 134 alive / 23 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 199 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42404
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
