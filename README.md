# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 430
- HTTP: 121 alive / 81 gold
- HTTPS: 88 alive / 22 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34129
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
