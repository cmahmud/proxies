# SyndProxy private pool

## Current pool

- Alive now: 820
- Gold now: 395
- HTTP: 238 alive / 89 gold
- HTTPS: 166 alive / 28 gold
- SOCKS4: 203 alive / 140 gold
- SOCKS5: 213 alive / 138 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31620
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
