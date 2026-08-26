# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 404
- HTTP: 97 alive / 66 gold
- HTTPS: 79 alive / 17 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38602
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
