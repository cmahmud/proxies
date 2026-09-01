# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 438
- HTTP: 98 alive / 72 gold
- HTTPS: 117 alive / 30 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 193 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47342
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
