# SyndProxy private pool

## Current pool

- Alive now: 857
- Gold now: 215
- HTTP: 307 alive / 28 gold
- HTTPS: 174 alive / 7 gold
- SOCKS4: 225 alive / 119 gold
- SOCKS5: 151 alive / 61 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13518
- Ever gold: 422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
