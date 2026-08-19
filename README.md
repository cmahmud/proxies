# SyndProxy private pool

## Current pool

- Alive now: 1127
- Gold now: 451
- HTTP: 427 alive / 119 gold
- HTTPS: 253 alive / 73 gold
- SOCKS4: 230 alive / 136 gold
- SOCKS5: 217 alive / 123 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16739
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
