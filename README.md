# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 405
- HTTP: 98 alive / 61 gold
- HTTPS: 76 alive / 15 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39114
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
