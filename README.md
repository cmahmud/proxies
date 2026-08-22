# SyndProxy private pool

## Current pool

- Alive now: 1124
- Gold now: 421
- HTTP: 389 alive / 99 gold
- HTTPS: 306 alive / 32 gold
- SOCKS4: 196 alive / 132 gold
- SOCKS5: 233 alive / 158 gold

## Historical pool

- Discovered: 161017
- Ever alive: 31099
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
