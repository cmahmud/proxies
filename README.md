# SyndProxy private pool

## Current pool

- Alive now: 1054
- Gold now: 504
- HTTP: 373 alive / 169 gold
- HTTPS: 238 alive / 48 gold
- SOCKS4: 223 alive / 143 gold
- SOCKS5: 220 alive / 144 gold

## Historical pool

- Discovered: 124827
- Ever alive: 19166
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
