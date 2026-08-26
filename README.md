# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 407
- HTTP: 111 alive / 65 gold
- HTTPS: 100 alive / 13 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 193 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38131
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
