# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 401
- HTTP: 356 alive / 77 gold
- HTTPS: 209 alive / 26 gold
- SOCKS4: 221 alive / 144 gold
- SOCKS5: 244 alive / 154 gold

## Historical pool

- Discovered: 156566
- Ever alive: 29563
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
