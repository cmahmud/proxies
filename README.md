# SyndProxy private pool

## Current pool

- Alive now: 814
- Gold now: 275
- HTTP: 209 alive / 28 gold
- HTTPS: 132 alive / 5 gold
- SOCKS4: 240 alive / 127 gold
- SOCKS5: 233 alive / 115 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12142
- Ever gold: 395

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
