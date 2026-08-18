# SyndProxy private pool

## Current pool

- Alive now: 829
- Gold now: 250
- HTTP: 379 alive / 27 gold
- HTTPS: 90 alive / 10 gold
- SOCKS4: 183 alive / 127 gold
- SOCKS5: 177 alive / 86 gold

## Historical pool

- Discovered: 94350
- Ever alive: 9921
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
