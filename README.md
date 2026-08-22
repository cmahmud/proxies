# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 374
- HTTP: 283 alive / 82 gold
- HTTPS: 213 alive / 22 gold
- SOCKS4: 220 alive / 142 gold
- SOCKS5: 231 alive / 128 gold

## Historical pool

- Discovered: 165822
- Ever alive: 32335
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
