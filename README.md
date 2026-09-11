# SyndProxy validated proxy pool

## Current pool

- Alive now: 447
- Gold now: 350
- HTTP: 82 alive / 69 gold
- HTTPS: 50 alive / 29 gold
- SOCKS4: 119 alive / 75 gold
- SOCKS5: 196 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48586
- Ever gold: 1557

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
