# SyndProxy private pool

## Current pool

- Alive now: 920
- Gold now: 347
- HTTP: 299 alive / 67 gold
- HTTPS: 193 alive / 15 gold
- SOCKS4: 224 alive / 142 gold
- SOCKS5: 204 alive / 123 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15278
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
