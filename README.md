# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 441
- HTTP: 94 alive / 75 gold
- HTTPS: 107 alive / 31 gold
- SOCKS4: 186 alive / 160 gold
- SOCKS5: 186 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47509
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
