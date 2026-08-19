# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 520
- HTTP: 415 alive / 159 gold
- HTTPS: 259 alive / 89 gold
- SOCKS4: 224 alive / 146 gold
- SOCKS5: 182 alive / 126 gold

## Historical pool

- Discovered: 123229
- Ever alive: 19003
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
