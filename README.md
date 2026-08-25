# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 401
- HTTP: 85 alive / 64 gold
- HTTPS: 68 alive / 20 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 172 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37648
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
