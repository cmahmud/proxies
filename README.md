# SyndProxy private pool

## Current pool

- Alive now: 855
- Gold now: 259
- HTTP: 242 alive / 29 gold
- HTTPS: 167 alive / 3 gold
- SOCKS4: 221 alive / 118 gold
- SOCKS5: 225 alive / 109 gold

## Historical pool

- Discovered: 99160
- Ever alive: 12099
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
