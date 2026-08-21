# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 400
- HTTP: 271 alive / 80 gold
- HTTPS: 159 alive / 26 gold
- SOCKS4: 223 alive / 144 gold
- SOCKS5: 238 alive / 150 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29584
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
