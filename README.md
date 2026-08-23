# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 364
- HTTP: 79 alive / 44 gold
- HTTPS: 52 alive / 9 gold
- SOCKS4: 175 alive / 155 gold
- SOCKS5: 195 alive / 156 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32996
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
