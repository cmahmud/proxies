# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 398
- HTTP: 101 alive / 70 gold
- HTTPS: 89 alive / 14 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 170 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43075
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
