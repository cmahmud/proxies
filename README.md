# SyndProxy validated proxy pool

## Current pool

- Alive now: 437
- Gold now: 336
- HTTP: 60 alive / 39 gold
- HTTPS: 40 alive / 7 gold
- SOCKS4: 167 alive / 147 gold
- SOCKS5: 170 alive / 143 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43531
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
