# SyndProxy private pool

## Current pool

- Alive now: 1175
- Gold now: 510
- HTTP: 457 alive / 176 gold
- HTTPS: 295 alive / 113 gold
- SOCKS4: 229 alive / 109 gold
- SOCKS5: 194 alive / 112 gold

## Historical pool

- Discovered: 124843
- Ever alive: 19333
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
