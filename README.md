# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 392
- HTTP: 97 alive / 62 gold
- HTTPS: 85 alive / 17 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 172 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37356
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
