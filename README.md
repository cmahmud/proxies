# SyndProxy validated proxy pool

## Current pool

- Alive now: 419
- Gold now: 344
- HTTP: 79 alive / 44 gold
- HTTPS: 38 alive / 9 gold
- SOCKS4: 151 alive / 146 gold
- SOCKS5: 151 alive / 145 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43636
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
