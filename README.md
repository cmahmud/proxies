# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 430
- HTTP: 110 alive / 66 gold
- HTTPS: 88 alive / 24 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 203 alive / 179 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35944
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
