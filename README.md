# SyndProxy private pool

## Current pool

- Alive now: 767
- Gold now: 414
- HTTP: 201 alive / 88 gold
- HTTPS: 149 alive / 28 gold
- SOCKS4: 194 alive / 139 gold
- SOCKS5: 223 alive / 159 gold

## Historical pool

- Discovered: 162443
- Ever alive: 31440
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
