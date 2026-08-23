# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 378
- HTTP: 84 alive / 55 gold
- HTTPS: 35 alive / 9 gold
- SOCKS4: 177 alive / 156 gold
- SOCKS5: 180 alive / 158 gold

## Historical pool

- Discovered: 174823
- Ever alive: 33104
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
