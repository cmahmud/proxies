# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 400
- HTTP: 95 alive / 64 gold
- HTTPS: 88 alive / 20 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 177 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37571
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
