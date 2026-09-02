# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 436
- HTTP: 127 alive / 75 gold
- HTTPS: 122 alive / 24 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47611
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
