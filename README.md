# SyndProxy private pool

## Current pool

- Alive now: 917
- Gold now: 290
- HTTP: 253 alive / 45 gold
- HTTPS: 218 alive / 8 gold
- SOCKS4: 225 alive / 112 gold
- SOCKS5: 221 alive / 125 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14481
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
