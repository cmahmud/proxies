# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 451
- HTTP: 92 alive / 74 gold
- HTTPS: 115 alive / 35 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 195 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47399
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
