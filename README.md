# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 436
- HTTP: 112 alive / 76 gold
- HTTPS: 98 alive / 22 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 184 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47588
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
