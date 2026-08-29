# SyndProxy validated proxy pool

## Current pool

- Alive now: 391
- Gold now: 289
- HTTP: 47 alive / 25 gold
- HTTPS: 14 alive / 1 gold
- SOCKS4: 159 alive / 138 gold
- SOCKS5: 171 alive / 125 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43594
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
