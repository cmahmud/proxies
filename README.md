# SyndProxy private pool

## Current pool

- Alive now: 1151
- Gold now: 509
- HTTP: 399 alive / 168 gold
- HTTPS: 313 alive / 84 gold
- SOCKS4: 223 alive / 130 gold
- SOCKS5: 216 alive / 127 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19762
- Ever gold: 778

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
