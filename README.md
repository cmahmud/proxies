# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 440
- HTTP: 89 alive / 74 gold
- HTTPS: 91 alive / 29 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 184 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47519
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
