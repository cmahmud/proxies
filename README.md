# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 431
- HTTP: 94 alive / 73 gold
- HTTPS: 111 alive / 22 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47668
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
