# SyndProxy private pool

## Current pool

- Alive now: 1153
- Gold now: 509
- HTTP: 447 alive / 175 gold
- HTTPS: 304 alive / 113 gold
- SOCKS4: 216 alive / 109 gold
- SOCKS5: 186 alive / 112 gold

## Historical pool

- Discovered: 124843
- Ever alive: 19332
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
