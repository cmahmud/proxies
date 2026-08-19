# SyndProxy private pool

## Current pool

- Alive now: 1163
- Gold now: 451
- HTTP: 451 alive / 118 gold
- HTTPS: 264 alive / 73 gold
- SOCKS4: 226 alive / 134 gold
- SOCKS5: 222 alive / 126 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16734
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
