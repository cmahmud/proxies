# SyndProxy validated proxy pool

## Current pool

- Alive now: 419
- Gold now: 344
- HTTP: 76 alive / 43 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 151 alive / 146 gold
- SOCKS5: 152 alive / 145 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43636
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
