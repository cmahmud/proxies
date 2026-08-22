# SyndProxy private pool

## Current pool

- Alive now: 995
- Gold now: 434
- HTTP: 303 alive / 95 gold
- HTTPS: 228 alive / 27 gold
- SOCKS4: 206 alive / 144 gold
- SOCKS5: 258 alive / 168 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31248
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
