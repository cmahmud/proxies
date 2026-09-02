# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 440
- HTTP: 96 alive / 69 gold
- HTTPS: 100 alive / 31 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 182 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47497
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
