# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 286
- HTTP: 210 alive / 28 gold
- HTTPS: 125 alive / 5 gold
- SOCKS4: 252 alive / 138 gold
- SOCKS5: 235 alive / 115 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12143
- Ever gold: 395

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
