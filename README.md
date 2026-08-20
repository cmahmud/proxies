# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 384
- HTTP: 177 alive / 78 gold
- HTTPS: 206 alive / 21 gold
- SOCKS4: 191 alive / 132 gold
- SOCKS5: 206 alive / 153 gold

## Historical pool

- Discovered: 151055
- Ever alive: 27210
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
