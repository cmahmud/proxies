# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 408
- HTTP: 107 alive / 66 gold
- HTTPS: 116 alive / 15 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38073
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
