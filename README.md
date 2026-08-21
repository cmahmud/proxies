# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 399
- HTTP: 319 alive / 101 gold
- HTTPS: 236 alive / 30 gold
- SOCKS4: 203 alive / 147 gold
- SOCKS5: 209 alive / 121 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28466
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
