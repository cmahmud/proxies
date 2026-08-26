# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 401
- HTTP: 97 alive / 61 gold
- HTTPS: 78 alive / 17 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 190 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38575
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
