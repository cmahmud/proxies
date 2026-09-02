# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 443
- HTTP: 105 alive / 81 gold
- HTTPS: 108 alive / 25 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 193 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47558
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
