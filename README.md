# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 438
- HTTP: 125 alive / 74 gold
- HTTPS: 104 alive / 28 gold
- SOCKS4: 188 alive / 165 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47643
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
