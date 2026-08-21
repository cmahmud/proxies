# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 327
- HTTP: 244 alive / 79 gold
- HTTPS: 125 alive / 21 gold
- SOCKS4: 174 alive / 105 gold
- SOCKS5: 201 alive / 122 gold

## Historical pool

- Discovered: 157573
- Ever alive: 29767
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
