# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 443
- HTTP: 98 alive / 79 gold
- HTTPS: 99 alive / 29 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 180 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47527
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
