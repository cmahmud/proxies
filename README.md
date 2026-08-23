# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 378
- HTTP: 84 alive / 54 gold
- HTTPS: 48 alive / 11 gold
- SOCKS4: 162 alive / 156 gold
- SOCKS5: 177 alive / 157 gold

## Historical pool

- Discovered: 175389
- Ever alive: 33123
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
