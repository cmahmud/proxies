# SyndProxy private pool

## Current pool

- Alive now: 1135
- Gold now: 524
- HTTP: 409 alive / 155 gold
- HTTPS: 276 alive / 94 gold
- SOCKS4: 241 alive / 149 gold
- SOCKS5: 209 alive / 126 gold

## Historical pool

- Discovered: 123176
- Ever alive: 18910
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
