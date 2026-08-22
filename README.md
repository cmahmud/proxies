# SyndProxy private pool

## Current pool

- Alive now: 1039
- Gold now: 417
- HTTP: 355 alive / 93 gold
- HTTPS: 267 alive / 33 gold
- SOCKS4: 184 alive / 130 gold
- SOCKS5: 233 alive / 161 gold

## Historical pool

- Discovered: 161344
- Ever alive: 31123
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
