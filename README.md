# SyndProxy private pool

## Current pool

- Alive now: 875
- Gold now: 432
- HTTP: 253 alive / 88 gold
- HTTPS: 174 alive / 32 gold
- SOCKS4: 200 alive / 147 gold
- SOCKS5: 248 alive / 165 gold

## Historical pool

- Discovered: 162748
- Ever alive: 31514
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
