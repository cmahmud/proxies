# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 420
- HTTP: 319 alive / 94 gold
- HTTPS: 221 alive / 24 gold
- SOCKS4: 227 alive / 151 gold
- SOCKS5: 248 alive / 151 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25172
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
