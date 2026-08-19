# SyndProxy private pool

## Current pool

- Alive now: 1129
- Gold now: 542
- HTTP: 438 alive / 163 gold
- HTTPS: 246 alive / 94 gold
- SOCKS4: 233 alive / 144 gold
- SOCKS5: 212 alive / 141 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18864
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
