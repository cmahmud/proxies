# SyndProxy private pool

## Current pool

- Alive now: 1215
- Gold now: 497
- HTTP: 424 alive / 145 gold
- HTTPS: 325 alive / 91 gold
- SOCKS4: 221 alive / 124 gold
- SOCKS5: 245 alive / 137 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17291
- Ever gold: 662

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
