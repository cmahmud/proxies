# SyndProxy validated proxy pool

## Current pool

- Alive now: 405
- Gold now: 339
- HTTP: 69 alive / 40 gold
- HTTPS: 35 alive / 8 gold
- SOCKS4: 150 alive / 146 gold
- SOCKS5: 151 alive / 145 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43636
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
