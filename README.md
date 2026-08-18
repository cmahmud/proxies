# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 289
- HTTP: 256 alive / 45 gold
- HTTPS: 215 alive / 8 gold
- SOCKS4: 222 alive / 111 gold
- SOCKS5: 220 alive / 125 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14481
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
