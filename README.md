# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 438
- HTTP: 93 alive / 71 gold
- HTTPS: 114 alive / 30 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47503
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
