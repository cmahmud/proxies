# SyndProxy private pool

## Current pool

- Alive now: 767
- Gold now: 357
- HTTP: 192 alive / 69 gold
- HTTPS: 142 alive / 20 gold
- SOCKS4: 224 alive / 145 gold
- SOCKS5: 209 alive / 123 gold

## Historical pool

- Discovered: 145547
- Ever alive: 25391
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
