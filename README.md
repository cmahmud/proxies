# SyndProxy private pool

## Current pool

- Alive now: 711
- Gold now: 381
- HTTP: 190 alive / 63 gold
- HTTPS: 105 alive / 18 gold
- SOCKS4: 203 alive / 147 gold
- SOCKS5: 213 alive / 153 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25693
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
