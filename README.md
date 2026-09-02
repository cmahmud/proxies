# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 437
- HTTP: 110 alive / 75 gold
- HTTPS: 99 alive / 27 gold
- SOCKS4: 185 alive / 161 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47569
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
