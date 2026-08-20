# SyndProxy private pool

## Current pool

- Alive now: 885
- Gold now: 405
- HTTP: 244 alive / 77 gold
- HTTPS: 202 alive / 23 gold
- SOCKS4: 210 alive / 148 gold
- SOCKS5: 229 alive / 157 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27146
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
