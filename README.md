# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 407
- HTTP: 100 alive / 61 gold
- HTTPS: 64 alive / 17 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38308
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
