# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 405
- HTTP: 272 alive / 96 gold
- HTTPS: 225 alive / 35 gold
- SOCKS4: 226 alive / 142 gold
- SOCKS5: 258 alive / 132 gold

## Historical pool

- Discovered: 160995
- Ever alive: 30934
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
