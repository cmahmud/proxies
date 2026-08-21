# SyndProxy private pool

## Current pool

- Alive now: 773
- Gold now: 402
- HTTP: 219 alive / 90 gold
- HTTPS: 153 alive / 25 gold
- SOCKS4: 186 alive / 128 gold
- SOCKS5: 215 alive / 159 gold

## Historical pool

- Discovered: 151684
- Ever alive: 27700
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
