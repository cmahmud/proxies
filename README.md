# SyndProxy private pool

## Current pool

- Alive now: 706
- Gold now: 376
- HTTP: 189 alive / 77 gold
- HTTPS: 131 alive / 19 gold
- SOCKS4: 205 alive / 149 gold
- SOCKS5: 181 alive / 131 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25931
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
