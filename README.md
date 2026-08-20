# SyndProxy private pool

## Current pool

- Alive now: 701
- Gold now: 377
- HTTP: 183 alive / 77 gold
- HTTPS: 130 alive / 19 gold
- SOCKS4: 207 alive / 150 gold
- SOCKS5: 181 alive / 131 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25931
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
