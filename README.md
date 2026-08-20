# SyndProxy private pool

## Current pool

- Alive now: 1338
- Gold now: 603
- HTTP: 505 alive / 202 gold
- HTTPS: 375 alive / 101 gold
- SOCKS4: 216 alive / 145 gold
- SOCKS5: 242 alive / 155 gold

## Historical pool

- Discovered: 138953
- Ever alive: 23399
- Ever gold: 920

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
