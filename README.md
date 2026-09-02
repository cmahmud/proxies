# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 438
- HTTP: 126 alive / 78 gold
- HTTPS: 101 alive / 26 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47643
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
