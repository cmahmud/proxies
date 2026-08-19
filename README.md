# SyndProxy private pool

## Current pool

- Alive now: 966
- Gold now: 484
- HTTP: 303 alive / 133 gold
- HTTPS: 248 alive / 83 gold
- SOCKS4: 204 alive / 126 gold
- SOCKS5: 211 alive / 142 gold

## Historical pool

- Discovered: 117155
- Ever alive: 17562
- Ever gold: 679

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
