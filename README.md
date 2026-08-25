# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 417
- HTTP: 108 alive / 72 gold
- HTTPS: 94 alive / 20 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35055
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
