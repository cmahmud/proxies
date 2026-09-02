# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 441
- HTTP: 92 alive / 74 gold
- HTTPS: 106 alive / 32 gold
- SOCKS4: 183 alive / 160 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47508
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
