# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 350
- HTTP: 124 alive / 73 gold
- HTTPS: 69 alive / 22 gold
- SOCKS4: 132 alive / 112 gold
- SOCKS5: 171 alive / 143 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47984
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
