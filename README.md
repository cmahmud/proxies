# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 534
- HTTP: 371 alive / 164 gold
- HTTPS: 255 alive / 94 gold
- SOCKS4: 235 alive / 147 gold
- SOCKS5: 218 alive / 129 gold

## Historical pool

- Discovered: 123228
- Ever alive: 18972
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
