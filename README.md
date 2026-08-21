# SyndProxy private pool

## Current pool

- Alive now: 829
- Gold now: 394
- HTTP: 234 alive / 91 gold
- HTTPS: 191 alive / 20 gold
- SOCKS4: 194 alive / 137 gold
- SOCKS5: 210 alive / 146 gold

## Historical pool

- Discovered: 152166
- Ever alive: 27875
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
