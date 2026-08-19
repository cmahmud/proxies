# SyndProxy private pool

## Current pool

- Alive now: 1204
- Gold now: 532
- HTTP: 450 alive / 156 gold
- HTTPS: 321 alive / 106 gold
- SOCKS4: 226 alive / 142 gold
- SOCKS5: 207 alive / 128 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19943
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
