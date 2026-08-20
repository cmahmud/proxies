# SyndProxy private pool

## Current pool

- Alive now: 995
- Gold now: 373
- HTTP: 303 alive / 87 gold
- HTTPS: 242 alive / 23 gold
- SOCKS4: 200 alive / 130 gold
- SOCKS5: 250 alive / 133 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25040
- Ever gold: 1053

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
