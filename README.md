# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 326
- HTTP: 338 alive / 53 gold
- HTTPS: 202 alive / 12 gold
- SOCKS4: 213 alive / 131 gold
- SOCKS5: 203 alive / 130 gold

## Historical pool

- Discovered: 129233
- Ever alive: 20034
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
