# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 421
- HTTP: 109 alive / 62 gold
- HTTPS: 105 alive / 24 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 200 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35848
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
