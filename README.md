# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 401
- HTTP: 85 alive / 58 gold
- HTTPS: 76 alive / 16 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39191
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
