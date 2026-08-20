# SyndProxy private pool

## Current pool

- Alive now: 773
- Gold now: 377
- HTTP: 180 alive / 76 gold
- HTTPS: 177 alive / 19 gold
- SOCKS4: 204 alive / 144 gold
- SOCKS5: 212 alive / 138 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26139
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
