# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 380
- HTTP: 82 alive / 56 gold
- HTTPS: 39 alive / 10 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 177 alive / 158 gold

## Historical pool

- Discovered: 174823
- Ever alive: 33104
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
