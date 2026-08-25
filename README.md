# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 418
- HTTP: 105 alive / 64 gold
- HTTPS: 83 alive / 22 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35534
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
