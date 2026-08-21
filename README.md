# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 383
- HTTP: 266 alive / 71 gold
- HTTPS: 190 alive / 18 gold
- SOCKS4: 223 alive / 143 gold
- SOCKS5: 234 alive / 151 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29571
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
