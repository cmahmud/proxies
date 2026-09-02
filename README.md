# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 439
- HTTP: 91 alive / 73 gold
- HTTPS: 97 alive / 29 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 185 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47520
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
