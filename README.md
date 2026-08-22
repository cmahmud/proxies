# SyndProxy private pool

## Current pool

- Alive now: 949
- Gold now: 431
- HTTP: 278 alive / 87 gold
- HTTPS: 223 alive / 31 gold
- SOCKS4: 203 alive / 150 gold
- SOCKS5: 245 alive / 163 gold

## Historical pool

- Discovered: 162748
- Ever alive: 31533
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
