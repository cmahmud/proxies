# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 404
- HTTP: 69 alive / 50 gold
- HTTPS: 42 alive / 22 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47109
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
