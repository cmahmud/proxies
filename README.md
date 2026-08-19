# SyndProxy private pool

## Current pool

- Alive now: 1044
- Gold now: 541
- HTTP: 349 alive / 164 gold
- HTTPS: 250 alive / 95 gold
- SOCKS4: 237 alive / 145 gold
- SOCKS5: 208 alive / 137 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18891
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
