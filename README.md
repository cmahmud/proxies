# SyndProxy private pool

## Current pool

- Alive now: 839
- Gold now: 417
- HTTP: 235 alive / 88 gold
- HTTPS: 173 alive / 27 gold
- SOCKS4: 191 alive / 134 gold
- SOCKS5: 240 alive / 168 gold

## Historical pool

- Discovered: 162702
- Ever alive: 31461
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
