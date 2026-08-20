# SyndProxy private pool

## Current pool

- Alive now: 710
- Gold now: 376
- HTTP: 165 alive / 73 gold
- HTTPS: 135 alive / 20 gold
- SOCKS4: 202 alive / 138 gold
- SOCKS5: 208 alive / 145 gold

## Historical pool

- Discovered: 145568
- Ever alive: 25510
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
