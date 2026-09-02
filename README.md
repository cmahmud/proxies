# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 452
- HTTP: 102 alive / 78 gold
- HTTPS: 112 alive / 30 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 186 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47430
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
