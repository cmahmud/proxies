# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 370
- HTTP: 85 alive / 57 gold
- HTTPS: 61 alive / 17 gold
- SOCKS4: 157 alive / 142 gold
- SOCKS5: 171 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38880
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
