# SyndProxy private pool

## Current pool

- Alive now: 1114
- Gold now: 302
- HTTP: 430 alive / 31 gold
- HTTPS: 251 alive / 4 gold
- SOCKS4: 224 alive / 140 gold
- SOCKS5: 209 alive / 127 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13416
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
