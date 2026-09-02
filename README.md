# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 448
- HTTP: 116 alive / 80 gold
- HTTPS: 111 alive / 29 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 193 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47550
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
