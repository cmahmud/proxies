# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 414
- HTTP: 87 alive / 64 gold
- HTTPS: 107 alive / 19 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41466
- Ever gold: 1332

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
