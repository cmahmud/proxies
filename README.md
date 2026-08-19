# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 546
- HTTP: 363 alive / 163 gold
- HTTPS: 238 alive / 91 gold
- SOCKS4: 217 alive / 146 gold
- SOCKS5: 203 alive / 146 gold

## Historical pool

- Discovered: 123921
- Ever alive: 19153
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
