# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 433
- HTTP: 122 alive / 79 gold
- HTTPS: 113 alive / 24 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47655
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
