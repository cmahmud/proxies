# SyndProxy private pool

## Current pool

- Alive now: 1107
- Gold now: 526
- HTTP: 412 alive / 152 gold
- HTTPS: 253 alive / 89 gold
- SOCKS4: 217 alive / 149 gold
- SOCKS5: 225 alive / 136 gold

## Historical pool

- Discovered: 119810
- Ever alive: 18034
- Ever gold: 708

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
