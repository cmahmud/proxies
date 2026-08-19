# SyndProxy private pool

## Current pool

- Alive now: 1149
- Gold now: 540
- HTTP: 441 alive / 162 gold
- HTTPS: 273 alive / 91 gold
- SOCKS4: 227 alive / 144 gold
- SOCKS5: 208 alive / 143 gold

## Historical pool

- Discovered: 123921
- Ever alive: 19153
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
