# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 426
- HTTP: 167 alive / 76 gold
- HTTPS: 84 alive / 21 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 204 alive / 167 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33873
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
