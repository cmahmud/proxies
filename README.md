# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 421
- HTTP: 101 alive / 62 gold
- HTTPS: 97 alive / 21 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 213 alive / 177 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35907
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
