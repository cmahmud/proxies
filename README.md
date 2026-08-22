# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 399
- HTTP: 289 alive / 81 gold
- HTTPS: 164 alive / 25 gold
- SOCKS4: 229 alive / 149 gold
- SOCKS5: 232 alive / 144 gold

## Historical pool

- Discovered: 165872
- Ever alive: 32378
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
