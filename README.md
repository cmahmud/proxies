# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 394
- HTTP: 162 alive / 67 gold
- HTTPS: 115 alive / 21 gold
- SOCKS4: 164 alive / 150 gold
- SOCKS5: 195 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39516
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
