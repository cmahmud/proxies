# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 421
- HTTP: 99 alive / 61 gold
- HTTPS: 99 alive / 25 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 198 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35842
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
