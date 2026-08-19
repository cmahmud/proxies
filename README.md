# SyndProxy private pool

## Current pool

- Alive now: 1057
- Gold now: 529
- HTTP: 380 alive / 162 gold
- HTTPS: 248 alive / 93 gold
- SOCKS4: 224 alive / 149 gold
- SOCKS5: 205 alive / 125 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18980
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
