# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 526
- HTTP: 361 alive / 162 gold
- HTTPS: 254 alive / 94 gold
- SOCKS4: 239 alive / 143 gold
- SOCKS5: 210 alive / 127 gold

## Historical pool

- Discovered: 123226
- Ever alive: 18930
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
