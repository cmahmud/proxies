# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 441
- HTTP: 95 alive / 70 gold
- HTTPS: 97 alive / 31 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 186 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47496
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
