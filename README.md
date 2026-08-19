# SyndProxy private pool

## Current pool

- Alive now: 934
- Gold now: 342
- HTTP: 302 alive / 68 gold
- HTTPS: 203 alive / 16 gold
- SOCKS4: 202 alive / 112 gold
- SOCKS5: 227 alive / 146 gold

## Historical pool

- Discovered: 111011
- Ever alive: 16184
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
