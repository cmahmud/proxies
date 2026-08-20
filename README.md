# SyndProxy private pool

## Current pool

- Alive now: 767
- Gold now: 390
- HTTP: 188 alive / 73 gold
- HTTPS: 147 alive / 19 gold
- SOCKS4: 221 alive / 150 gold
- SOCKS5: 211 alive / 148 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26281
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
