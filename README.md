# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 393
- HTTP: 106 alive / 64 gold
- HTTPS: 47 alive / 15 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 176 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38937
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
