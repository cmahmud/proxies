# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 392
- HTTP: 106 alive / 64 gold
- HTTPS: 64 alive / 19 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 164 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37498
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
