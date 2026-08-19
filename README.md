# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 524
- HTTP: 380 alive / 161 gold
- HTTPS: 229 alive / 89 gold
- SOCKS4: 221 alive / 147 gold
- SOCKS5: 188 alive / 127 gold

## Historical pool

- Discovered: 123233
- Ever alive: 19005
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
