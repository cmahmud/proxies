# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 529
- HTTP: 424 alive / 159 gold
- HTTPS: 268 alive / 91 gold
- SOCKS4: 228 alive / 152 gold
- SOCKS5: 176 alive / 127 gold

## Historical pool

- Discovered: 123229
- Ever alive: 19000
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
