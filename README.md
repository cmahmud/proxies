# SyndProxy private pool

## Current pool

- Alive now: 831
- Gold now: 283
- HTTP: 272 alive / 36 gold
- HTTPS: 181 alive / 9 gold
- SOCKS4: 211 alive / 139 gold
- SOCKS5: 167 alive / 99 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13958
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
