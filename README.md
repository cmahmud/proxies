# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 435
- HTTP: 107 alive / 76 gold
- HTTPS: 73 alive / 25 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 182 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47680
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
