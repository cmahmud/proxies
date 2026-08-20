# SyndProxy private pool

## Current pool

- Alive now: 1002
- Gold now: 375
- HTTP: 306 alive / 87 gold
- HTTPS: 244 alive / 25 gold
- SOCKS4: 202 alive / 130 gold
- SOCKS5: 250 alive / 133 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25040
- Ever gold: 1053

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
