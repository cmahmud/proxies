# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 437
- HTTP: 113 alive / 76 gold
- HTTPS: 91 alive / 22 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47599
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
