# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 393
- HTTP: 97 alive / 55 gold
- HTTPS: 57 alive / 13 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33553
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
