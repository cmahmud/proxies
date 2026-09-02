# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 435
- HTTP: 117 alive / 77 gold
- HTTPS: 109 alive / 22 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47583
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
