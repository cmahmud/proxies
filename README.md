# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 401
- HTTP: 107 alive / 69 gold
- HTTPS: 66 alive / 14 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 173 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37322
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
