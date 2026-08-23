# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 377
- HTTP: 82 alive / 54 gold
- HTTPS: 32 alive / 9 gold
- SOCKS4: 175 alive / 156 gold
- SOCKS5: 179 alive / 158 gold

## Historical pool

- Discovered: 174823
- Ever alive: 33104
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
