# SyndProxy private pool

## Current pool

- Alive now: 717
- Gold now: 378
- HTTP: 193 alive / 62 gold
- HTTPS: 103 alive / 17 gold
- SOCKS4: 208 alive / 146 gold
- SOCKS5: 213 alive / 153 gold

## Historical pool

- Discovered: 146656
- Ever alive: 25693
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
