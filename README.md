# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 398
- HTTP: 106 alive / 61 gold
- HTTPS: 84 alive / 12 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 193 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38350
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
