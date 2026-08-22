# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 386
- HTTP: 248 alive / 98 gold
- HTTPS: 169 alive / 25 gold
- SOCKS4: 200 alive / 135 gold
- SOCKS5: 196 alive / 128 gold

## Historical pool

- Discovered: 162755
- Ever alive: 31579
- Ever gold: 1162

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
