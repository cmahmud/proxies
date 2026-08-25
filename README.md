# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 429
- HTTP: 120 alive / 78 gold
- HTTPS: 99 alive / 24 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34890
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
