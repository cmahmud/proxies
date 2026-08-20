# SyndProxy private pool

## Current pool

- Alive now: 773
- Gold now: 386
- HTTP: 186 alive / 77 gold
- HTTPS: 168 alive / 26 gold
- SOCKS4: 205 alive / 127 gold
- SOCKS5: 214 alive / 156 gold

## Historical pool

- Discovered: 150519
- Ever alive: 27065
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
