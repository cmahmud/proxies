# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 442
- HTTP: 115 alive / 80 gold
- HTTPS: 100 alive / 33 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44629
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
