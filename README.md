# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 457
- HTTP: 132 alive / 87 gold
- HTTPS: 122 alive / 33 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 196 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46772
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
