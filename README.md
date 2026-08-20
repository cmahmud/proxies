# SyndProxy private pool

## Current pool

- Alive now: 745
- Gold now: 405
- HTTP: 203 alive / 84 gold
- HTTPS: 142 alive / 23 gold
- SOCKS4: 194 alive / 144 gold
- SOCKS5: 206 alive / 154 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27405
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
