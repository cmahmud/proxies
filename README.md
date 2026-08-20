# SyndProxy private pool

## Current pool

- Alive now: 701
- Gold now: 384
- HTTP: 184 alive / 78 gold
- HTTPS: 105 alive / 17 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 202 alive / 140 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25945
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
