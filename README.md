# SyndProxy private pool

## Current pool

- Alive now: 1146
- Gold now: 558
- HTTP: 396 alive / 165 gold
- HTTPS: 293 alive / 91 gold
- SOCKS4: 234 alive / 152 gold
- SOCKS5: 223 alive / 150 gold

## Historical pool

- Discovered: 123175
- Ever alive: 18895
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
