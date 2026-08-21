# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 410
- HTTP: 300 alive / 96 gold
- HTTPS: 222 alive / 33 gold
- SOCKS4: 224 alive / 147 gold
- SOCKS5: 242 alive / 134 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30972
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
