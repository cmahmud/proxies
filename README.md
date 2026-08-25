# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 398
- HTTP: 101 alive / 68 gold
- HTTPS: 84 alive / 18 gold
- SOCKS4: 164 alive / 156 gold
- SOCKS5: 171 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37433
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
