# SyndProxy private pool

## Current pool

- Alive now: 1168
- Gold now: 392
- HTTP: 446 alive / 104 gold
- HTTPS: 248 alive / 23 gold
- SOCKS4: 216 alive / 127 gold
- SOCKS5: 258 alive / 138 gold

## Historical pool

- Discovered: 152217
- Ever alive: 27966
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
