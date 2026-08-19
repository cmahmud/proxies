# SyndProxy private pool

## Current pool

- Alive now: 1208
- Gold now: 398
- HTTP: 391 alive / 90 gold
- HTTPS: 294 alive / 20 gold
- SOCKS4: 233 alive / 137 gold
- SOCKS5: 290 alive / 151 gold

## Historical pool

- Discovered: 134569
- Ever alive: 22180
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
