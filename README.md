# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 438
- HTTP: 94 alive / 71 gold
- HTTPS: 100 alive / 28 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 189 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47460
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
