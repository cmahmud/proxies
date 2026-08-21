# SyndProxy private pool

## Current pool

- Alive now: 1201
- Gold now: 440
- HTTP: 432 alive / 108 gold
- HTTPS: 303 alive / 33 gold
- SOCKS4: 210 alive / 153 gold
- SOCKS5: 256 alive / 146 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28627
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
