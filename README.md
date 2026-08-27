# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 409
- HTTP: 115 alive / 59 gold
- HTTPS: 144 alive / 18 gold
- SOCKS4: 180 alive / 165 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41270
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
