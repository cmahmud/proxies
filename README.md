# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 438
- HTTP: 86 alive / 69 gold
- HTTPS: 95 alive / 30 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 191 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47462
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
