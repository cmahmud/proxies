# SyndProxy private pool

## Current pool

- Alive now: 1121
- Gold now: 593
- HTTP: 371 alive / 188 gold
- HTTPS: 304 alive / 101 gold
- SOCKS4: 209 alive / 146 gold
- SOCKS5: 237 alive / 158 gold

## Historical pool

- Discovered: 138957
- Ever alive: 23453
- Ever gold: 921

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
