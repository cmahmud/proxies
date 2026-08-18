# SyndProxy private pool

## Current pool

- Alive now: 933
- Gold now: 310
- HTTP: 299 alive / 38 gold
- HTTPS: 185 alive / 9 gold
- SOCKS4: 225 alive / 138 gold
- SOCKS5: 224 alive / 125 gold

## Historical pool

- Discovered: 106998
- Ever alive: 14191
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
