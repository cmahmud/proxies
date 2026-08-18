# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 291
- HTTP: 275 alive / 26 gold
- HTTPS: 166 alive / 4 gold
- SOCKS4: 220 alive / 144 gold
- SOCKS5: 221 alive / 117 gold

## Historical pool

- Discovered: 102812
- Ever alive: 12776
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
