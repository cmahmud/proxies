# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 431
- HTTP: 128 alive / 81 gold
- HTTPS: 149 alive / 23 gold
- SOCKS4: 185 alive / 159 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42344
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
