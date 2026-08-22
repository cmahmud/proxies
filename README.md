# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 426
- HTTP: 383 alive / 103 gold
- HTTPS: 273 alive / 31 gold
- SOCKS4: 192 alive / 135 gold
- SOCKS5: 248 alive / 157 gold

## Historical pool

- Discovered: 161019
- Ever alive: 31111
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
