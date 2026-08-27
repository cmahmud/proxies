# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 412
- HTTP: 99 alive / 61 gold
- HTTPS: 105 alive / 20 gold
- SOCKS4: 174 alive / 165 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41477
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
