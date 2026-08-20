# SyndProxy private pool

## Current pool

- Alive now: 1202
- Gold now: 560
- HTTP: 427 alive / 182 gold
- HTTPS: 313 alive / 96 gold
- SOCKS4: 211 alive / 129 gold
- SOCKS5: 251 alive / 153 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22949
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
