# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 375
- HTTP: 330 alive / 67 gold
- HTTPS: 250 alive / 19 gold
- SOCKS4: 199 alive / 128 gold
- SOCKS5: 250 alive / 161 gold

## Historical pool

- Discovered: 110439
- Ever alive: 15749
- Ever gold: 503

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
