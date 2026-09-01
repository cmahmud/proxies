# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 467
- HTTP: 125 alive / 95 gold
- HTTPS: 114 alive / 35 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 204 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46385
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
