# SyndProxy private pool

## Current pool

- Alive now: 1067
- Gold now: 526
- HTTP: 373 alive / 164 gold
- HTTPS: 286 alive / 91 gold
- SOCKS4: 189 alive / 123 gold
- SOCKS5: 219 alive / 148 gold

## Historical pool

- Discovered: 124834
- Ever alive: 19199
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
