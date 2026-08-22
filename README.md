# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 404
- HTTP: 255 alive / 96 gold
- HTTPS: 187 alive / 30 gold
- SOCKS4: 223 alive / 146 gold
- SOCKS5: 239 alive / 132 gold

## Historical pool

- Discovered: 161992
- Ever alive: 31305
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
