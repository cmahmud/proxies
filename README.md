# SyndProxy private pool

## Current pool

- Alive now: 1115
- Gold now: 508
- HTTP: 432 alive / 176 gold
- HTTPS: 269 alive / 112 gold
- SOCKS4: 223 alive / 109 gold
- SOCKS5: 191 alive / 111 gold

## Historical pool

- Discovered: 124843
- Ever alive: 19333
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
