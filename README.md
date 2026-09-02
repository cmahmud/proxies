# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 440
- HTTP: 88 alive / 75 gold
- HTTPS: 104 alive / 28 gold
- SOCKS4: 184 alive / 162 gold
- SOCKS5: 187 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47517
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
