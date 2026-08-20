# SyndProxy private pool

## Current pool

- Alive now: 663
- Gold now: 383
- HTTP: 180 alive / 67 gold
- HTTPS: 97 alive / 17 gold
- SOCKS4: 194 alive / 150 gold
- SOCKS5: 192 alive / 149 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25704
- Ever gold: 1072

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
