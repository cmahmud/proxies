# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 401
- HTTP: 108 alive / 60 gold
- HTTPS: 63 alive / 18 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38727
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
