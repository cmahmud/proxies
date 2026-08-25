# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 417
- HTTP: 98 alive / 65 gold
- HTTPS: 76 alive / 22 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35493
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
