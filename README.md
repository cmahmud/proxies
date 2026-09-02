# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 430
- HTTP: 92 alive / 72 gold
- HTTPS: 83 alive / 23 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 180 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47681
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
