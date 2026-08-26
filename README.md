# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 421
- HTTP: 107 alive / 73 gold
- HTTPS: 87 alive / 20 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37981
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
