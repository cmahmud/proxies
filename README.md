# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 520
- HTTP: 386 alive / 157 gold
- HTTPS: 269 alive / 90 gold
- SOCKS4: 227 alive / 149 gold
- SOCKS5: 193 alive / 124 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18998
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
