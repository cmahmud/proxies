# SyndProxy private pool

## Current pool

- Alive now: 1101
- Gold now: 547
- HTTP: 403 alive / 164 gold
- HTTPS: 267 alive / 89 gold
- SOCKS4: 221 alive / 148 gold
- SOCKS5: 210 alive / 146 gold

## Historical pool

- Discovered: 123237
- Ever alive: 19086
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
