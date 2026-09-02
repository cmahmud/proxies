# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 445
- HTTP: 141 alive / 79 gold
- HTTPS: 118 alive / 27 gold
- SOCKS4: 186 alive / 165 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47630
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
