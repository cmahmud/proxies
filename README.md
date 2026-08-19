# SyndProxy private pool

## Current pool

- Alive now: 1144
- Gold now: 560
- HTTP: 444 alive / 170 gold
- HTTPS: 310 alive / 132 gold
- SOCKS4: 200 alive / 124 gold
- SOCKS5: 190 alive / 134 gold

## Historical pool

- Discovered: 127417
- Ever alive: 19965
- Ever gold: 861

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
