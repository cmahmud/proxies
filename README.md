# SyndProxy private pool

## Current pool

- Alive now: 1117
- Gold now: 452
- HTTP: 421 alive / 119 gold
- HTTPS: 250 alive / 73 gold
- SOCKS4: 225 alive / 136 gold
- SOCKS5: 221 alive / 124 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16738
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
