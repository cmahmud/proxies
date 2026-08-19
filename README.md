# SyndProxy private pool

## Current pool

- Alive now: 1067
- Gold now: 537
- HTTP: 377 alive / 160 gold
- HTTPS: 252 alive / 94 gold
- SOCKS4: 231 alive / 147 gold
- SOCKS5: 207 alive / 136 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18878
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
