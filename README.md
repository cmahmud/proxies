# SyndProxy private pool

## Current pool

- Alive now: 1070
- Gold now: 559
- HTTP: 353 alive / 166 gold
- HTTPS: 267 alive / 92 gold
- SOCKS4: 233 alive / 151 gold
- SOCKS5: 217 alive / 150 gold

## Historical pool

- Discovered: 123175
- Ever alive: 18896
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
