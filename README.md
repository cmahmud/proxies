# SyndProxy private pool

## Current pool

- Alive now: 1175
- Gold now: 568
- HTTP: 416 alive / 186 gold
- HTTPS: 304 alive / 97 gold
- SOCKS4: 207 alive / 127 gold
- SOCKS5: 248 alive / 158 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22949
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
