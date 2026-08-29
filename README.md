# SyndProxy validated proxy pool

## Current pool

- Alive now: 374
- Gold now: 299
- HTTP: 44 alive / 25 gold
- HTTPS: 7 alive / 0 gold
- SOCKS4: 159 alive / 136 gold
- SOCKS5: 164 alive / 138 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43603
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
