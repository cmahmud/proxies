# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 443
- HTTP: 105 alive / 81 gold
- HTTPS: 106 alive / 26 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 193 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47558
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
