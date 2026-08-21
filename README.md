# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 399
- HTTP: 329 alive / 77 gold
- HTTPS: 201 alive / 26 gold
- SOCKS4: 222 alive / 144 gold
- SOCKS5: 251 alive / 152 gold

## Historical pool

- Discovered: 156566
- Ever alive: 29566
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
