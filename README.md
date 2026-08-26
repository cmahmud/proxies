# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 407
- HTTP: 117 alive / 65 gold
- HTTPS: 70 alive / 18 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 201 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38693
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
