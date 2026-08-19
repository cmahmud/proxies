# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 531
- HTTP: 374 alive / 161 gold
- HTTPS: 248 alive / 93 gold
- SOCKS4: 218 alive / 150 gold
- SOCKS5: 203 alive / 127 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18984
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
