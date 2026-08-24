# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 376
- HTTP: 91 alive / 51 gold
- HTTPS: 71 alive / 10 gold
- SOCKS4: 173 alive / 156 gold
- SOCKS5: 177 alive / 159 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33444
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
