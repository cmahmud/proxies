# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 398
- HTTP: 100 alive / 75 gold
- HTTPS: 86 alive / 10 gold
- SOCKS4: 159 alive / 157 gold
- SOCKS5: 171 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43110
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
