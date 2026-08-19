# SyndProxy private pool

## Current pool

- Alive now: 1023
- Gold now: 529
- HTTP: 358 alive / 161 gold
- HTTPS: 249 alive / 94 gold
- SOCKS4: 209 alive / 149 gold
- SOCKS5: 207 alive / 125 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18990
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
