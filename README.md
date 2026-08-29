# SyndProxy validated proxy pool

## Current pool

- Alive now: 356
- Gold now: 293
- HTTP: 37 alive / 23 gold
- HTTPS: 4 alive / 0 gold
- SOCKS4: 156 alive / 138 gold
- SOCKS5: 159 alive / 132 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43617
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
