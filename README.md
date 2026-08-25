# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 420
- HTTP: 100 alive / 64 gold
- HTTPS: 99 alive / 23 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35587
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
