# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 435
- HTTP: 115 alive / 77 gold
- HTTPS: 102 alive / 22 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47584
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
