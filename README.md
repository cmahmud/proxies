# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 396
- HTTP: 95 alive / 64 gold
- HTTPS: 66 alive / 21 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 173 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37510
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
