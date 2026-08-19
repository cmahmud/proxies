# SyndProxy private pool

## Current pool

- Alive now: 1170
- Gold now: 539
- HTTP: 456 alive / 161 gold
- HTTPS: 253 alive / 94 gold
- SOCKS4: 246 alive / 144 gold
- SOCKS5: 215 alive / 140 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18867
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
