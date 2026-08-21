# SyndProxy private pool

## Current pool

- Alive now: 920
- Gold now: 392
- HTTP: 291 alive / 77 gold
- HTTPS: 171 alive / 23 gold
- SOCKS4: 226 alive / 144 gold
- SOCKS5: 232 alive / 148 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29584
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
