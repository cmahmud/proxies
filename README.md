# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 451
- HTTP: 92 alive / 74 gold
- HTTPS: 113 alive / 35 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 192 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47401
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
