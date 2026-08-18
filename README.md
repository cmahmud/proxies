# SyndProxy private pool

## Current pool

- Alive now: 591
- Gold now: 224
- HTTP: 167 alive / 32 gold
- HTTPS: 73 alive / 8 gold
- SOCKS4: 172 alive / 107 gold
- SOCKS5: 179 alive / 77 gold

## Historical pool

- Discovered: 86710
- Ever alive: 6454
- Ever gold: 300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
