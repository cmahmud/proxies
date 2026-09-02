# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 443
- HTTP: 124 alive / 78 gold
- HTTPS: 121 alive / 27 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47565
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
