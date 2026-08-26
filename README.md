# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 396
- HTTP: 111 alive / 64 gold
- HTTPS: 47 alive / 16 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38936
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
