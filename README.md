# SyndProxy private pool

## Current pool

- Alive now: 1154
- Gold now: 601
- HTTP: 444 alive / 190 gold
- HTTPS: 264 alive / 112 gold
- SOCKS4: 223 alive / 146 gold
- SOCKS5: 223 alive / 153 gold

## Historical pool

- Discovered: 124855
- Ever alive: 19425
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
