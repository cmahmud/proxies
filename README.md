# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 380
- HTTP: 86 alive / 63 gold
- HTTPS: 56 alive / 18 gold
- SOCKS4: 155 alive / 145 gold
- SOCKS5: 169 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38905
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
