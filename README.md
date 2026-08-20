# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 380
- HTTP: 204 alive / 76 gold
- HTTPS: 147 alive / 18 gold
- SOCKS4: 212 alive / 146 gold
- SOCKS5: 220 alive / 140 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26299
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
