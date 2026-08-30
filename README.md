# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 439
- HTTP: 120 alive / 79 gold
- HTTPS: 94 alive / 31 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44626
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
