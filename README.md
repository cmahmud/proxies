# SyndProxy private pool

## Current pool

- Alive now: 1165
- Gold now: 435
- HTTP: 404 alive / 106 gold
- HTTPS: 293 alive / 33 gold
- SOCKS4: 200 alive / 142 gold
- SOCKS5: 268 alive / 154 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28648
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
