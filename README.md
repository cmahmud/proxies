# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 431
- HTTP: 103 alive / 73 gold
- HTTPS: 91 alive / 30 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47321
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
