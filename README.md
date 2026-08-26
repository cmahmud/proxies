# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 407
- HTTP: 84 alive / 64 gold
- HTTPS: 69 alive / 18 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39078
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
