# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 389
- HTTP: 89 alive / 67 gold
- HTTPS: 80 alive / 11 gold
- SOCKS4: 157 alive / 154 gold
- SOCKS5: 168 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43146
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
