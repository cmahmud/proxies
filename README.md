# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 421
- HTTP: 373 alive / 95 gold
- HTTPS: 258 alive / 34 gold
- SOCKS4: 195 alive / 131 gold
- SOCKS5: 239 alive / 161 gold

## Historical pool

- Discovered: 161344
- Ever alive: 31125
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
