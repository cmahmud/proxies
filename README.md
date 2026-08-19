# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 542
- HTTP: 386 alive / 170 gold
- HTTPS: 248 alive / 92 gold
- SOCKS4: 218 alive / 142 gold
- SOCKS5: 214 alive / 138 gold

## Historical pool

- Discovered: 123166
- Ever alive: 18787
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
