# SyndProxy private pool

## Current pool

- Alive now: 703
- Gold now: 375
- HTTP: 187 alive / 77 gold
- HTTPS: 128 alive / 18 gold
- SOCKS4: 206 alive / 149 gold
- SOCKS5: 182 alive / 131 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25929
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
