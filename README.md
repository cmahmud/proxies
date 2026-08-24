# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 388
- HTTP: 133 alive / 55 gold
- HTTPS: 76 alive / 15 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 186 alive / 162 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33608
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
