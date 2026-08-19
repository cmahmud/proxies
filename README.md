# SyndProxy private pool

## Current pool

- Alive now: 1120
- Gold now: 520
- HTTP: 432 alive / 157 gold
- HTTPS: 271 alive / 90 gold
- SOCKS4: 226 alive / 149 gold
- SOCKS5: 191 alive / 124 gold

## Historical pool

- Discovered: 123229
- Ever alive: 19000
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
