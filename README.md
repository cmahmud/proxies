# SyndProxy private pool

## Current pool

- Alive now: 695
- Gold now: 382
- HTTP: 168 alive / 67 gold
- HTTPS: 109 alive / 19 gold
- SOCKS4: 198 alive / 149 gold
- SOCKS5: 220 alive / 147 gold

## Historical pool

- Discovered: 147597
- Ever alive: 25853
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
