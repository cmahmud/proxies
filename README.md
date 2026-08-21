# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 408
- HTTP: 314 alive / 90 gold
- HTTPS: 210 alive / 29 gold
- SOCKS4: 223 alive / 143 gold
- SOCKS5: 240 alive / 146 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29718
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
