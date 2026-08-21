# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 398
- HTTP: 388 alive / 91 gold
- HTTPS: 226 alive / 20 gold
- SOCKS4: 212 alive / 141 gold
- SOCKS5: 221 alive / 146 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29743
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
