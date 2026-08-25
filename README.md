# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 419
- HTTP: 106 alive / 61 gold
- HTTPS: 101 alive / 25 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35807
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
