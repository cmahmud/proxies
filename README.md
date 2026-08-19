# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 483
- HTTP: 304 alive / 132 gold
- HTTPS: 250 alive / 83 gold
- SOCKS4: 208 alive / 126 gold
- SOCKS5: 220 alive / 142 gold

## Historical pool

- Discovered: 117147
- Ever alive: 17562
- Ever gold: 679

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
