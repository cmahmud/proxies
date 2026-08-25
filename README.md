# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 419
- HTTP: 95 alive / 64 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 184 alive / 174 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35607
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
