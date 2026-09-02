# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 437
- HTTP: 110 alive / 78 gold
- HTTPS: 87 alive / 23 gold
- SOCKS4: 186 alive / 162 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47576
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
