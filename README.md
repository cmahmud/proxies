# SyndProxy private pool

## Current pool

- Alive now: 1169
- Gold now: 553
- HTTP: 419 alive / 164 gold
- HTTPS: 284 alive / 94 gold
- SOCKS4: 240 alive / 149 gold
- SOCKS5: 226 alive / 146 gold

## Historical pool

- Discovered: 123175
- Ever alive: 18907
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
