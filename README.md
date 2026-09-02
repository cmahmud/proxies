# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 447
- HTTP: 93 alive / 72 gold
- HTTPS: 96 alive / 34 gold
- SOCKS4: 176 alive / 164 gold
- SOCKS5: 185 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47486
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
