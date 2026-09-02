# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 448
- HTTP: 111 alive / 80 gold
- HTTPS: 116 alive / 29 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 192 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47549
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
