# SyndProxy private pool

## Current pool

- Alive now: 893
- Gold now: 389
- HTTP: 282 alive / 83 gold
- HTTPS: 190 alive / 21 gold
- SOCKS4: 208 alive / 145 gold
- SOCKS5: 213 alive / 140 gold

## Historical pool

- Discovered: 144823
- Ever alive: 25313
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
