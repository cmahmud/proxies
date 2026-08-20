# SyndProxy private pool

## Current pool

- Alive now: 819
- Gold now: 407
- HTTP: 220 alive / 74 gold
- HTTPS: 175 alive / 22 gold
- SOCKS4: 215 alive / 157 gold
- SOCKS5: 209 alive / 154 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27395
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
