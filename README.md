# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 421
- HTTP: 95 alive / 62 gold
- HTTPS: 102 alive / 25 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35828
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
