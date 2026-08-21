# SyndProxy private pool

## Current pool

- Alive now: 1099
- Gold now: 455
- HTTP: 368 alive / 112 gold
- HTTPS: 263 alive / 33 gold
- SOCKS4: 204 alive / 154 gold
- SOCKS5: 264 alive / 156 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28648
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
