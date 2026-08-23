# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 375
- HTTP: 90 alive / 60 gold
- HTTPS: 40 alive / 11 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 179 alive / 153 gold

## Historical pool

- Discovered: 174140
- Ever alive: 33066
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
