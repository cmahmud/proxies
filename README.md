# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 372
- HTTP: 79 alive / 47 gold
- HTTPS: 38 alive / 10 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 185 alive / 159 gold

## Historical pool

- Discovered: 173062
- Ever alive: 33006
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
