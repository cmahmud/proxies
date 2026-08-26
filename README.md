# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 405
- HTTP: 95 alive / 61 gold
- HTTPS: 87 alive / 13 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38249
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
