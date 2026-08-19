# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 548
- HTTP: 367 alive / 161 gold
- HTTPS: 263 alive / 90 gold
- SOCKS4: 223 alive / 149 gold
- SOCKS5: 228 alive / 148 gold

## Historical pool

- Discovered: 123175
- Ever alive: 18895
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
