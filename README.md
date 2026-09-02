# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 446
- HTTP: 89 alive / 72 gold
- HTTPS: 131 alive / 33 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 186 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47484
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
