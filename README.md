# SyndProxy private pool

## Current pool

- Alive now: 1852
- Gold now: 639
- HTTP: 712 alive / 228 gold
- HTTPS: 576 alive / 100 gold
- SOCKS4: 246 alive / 148 gold
- SOCKS5: 318 alive / 163 gold

## Historical pool

- Discovered: 142698
- Ever alive: 24335
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
