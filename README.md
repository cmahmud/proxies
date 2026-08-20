# SyndProxy private pool

## Current pool

- Alive now: 1834
- Gold now: 638
- HTTP: 702 alive / 228 gold
- HTTPS: 572 alive / 101 gold
- SOCKS4: 246 alive / 147 gold
- SOCKS5: 314 alive / 162 gold

## Historical pool

- Discovered: 142698
- Ever alive: 24329
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
