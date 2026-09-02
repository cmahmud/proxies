# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 431
- HTTP: 121 alive / 73 gold
- HTTPS: 105 alive / 22 gold
- SOCKS4: 176 alive / 165 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47602
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
