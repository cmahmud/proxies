# SyndProxy private pool

## Current pool

- Alive now: 1106
- Gold now: 550
- HTTP: 377 alive / 160 gold
- HTTPS: 267 alive / 90 gold
- SOCKS4: 230 alive / 151 gold
- SOCKS5: 232 alive / 149 gold

## Historical pool

- Discovered: 123171
- Ever alive: 18895
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
