# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 455
- HTTP: 320 alive / 111 gold
- HTTPS: 196 alive / 31 gold
- SOCKS4: 213 alive / 153 gold
- SOCKS5: 250 alive / 160 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28585
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
