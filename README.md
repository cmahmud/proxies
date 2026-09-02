# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 441
- HTTP: 98 alive / 75 gold
- HTTPS: 110 alive / 29 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 186 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47512
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
