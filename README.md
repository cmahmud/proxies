# SyndProxy private pool

## Current pool

- Alive now: 990
- Gold now: 554
- HTTP: 340 alive / 172 gold
- HTTPS: 227 alive / 90 gold
- SOCKS4: 210 alive / 145 gold
- SOCKS5: 213 alive / 147 gold

## Historical pool

- Discovered: 124825
- Ever alive: 19160
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
