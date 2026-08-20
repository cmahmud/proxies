# SyndProxy private pool

## Current pool

- Alive now: 701
- Gold now: 378
- HTTP: 162 alive / 74 gold
- HTTPS: 128 alive / 19 gold
- SOCKS4: 203 alive / 138 gold
- SOCKS5: 208 alive / 147 gold

## Historical pool

- Discovered: 145568
- Ever alive: 25510
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
