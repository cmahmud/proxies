# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 433
- HTTP: 106 alive / 75 gold
- HTTPS: 75 alive / 25 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 182 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47680
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
