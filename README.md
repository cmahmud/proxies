# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 437
- HTTP: 106 alive / 75 gold
- HTTPS: 101 alive / 27 gold
- SOCKS4: 186 alive / 161 gold
- SOCKS5: 196 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47568
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
