# SyndProxy private pool

## Current pool

- Alive now: 1099
- Gold now: 383
- HTTP: 392 alive / 103 gold
- HTTPS: 274 alive / 25 gold
- SOCKS4: 191 alive / 117 gold
- SOCKS5: 242 alive / 138 gold

## Historical pool

- Discovered: 152754
- Ever alive: 28278
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
