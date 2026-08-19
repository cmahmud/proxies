# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 524
- HTTP: 411 alive / 161 gold
- HTTPS: 256 alive / 89 gold
- SOCKS4: 219 alive / 147 gold
- SOCKS5: 188 alive / 127 gold

## Historical pool

- Discovered: 123233
- Ever alive: 19005
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
