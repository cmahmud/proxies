# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 445
- HTTP: 94 alive / 71 gold
- HTTPS: 96 alive / 31 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 193 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47468
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
