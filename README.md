# SyndProxy private pool

## Current pool

- Alive now: 773
- Gold now: 267
- HTTP: 217 alive / 26 gold
- HTTPS: 137 alive / 3 gold
- SOCKS4: 225 alive / 134 gold
- SOCKS5: 194 alive / 104 gold

## Historical pool

- Discovered: 99079
- Ever alive: 11472
- Ever gold: 383

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
