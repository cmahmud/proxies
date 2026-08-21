# SyndProxy private pool

## Current pool

- Alive now: 902
- Gold now: 372
- HTTP: 288 alive / 93 gold
- HTTPS: 191 alive / 25 gold
- SOCKS4: 205 alive / 140 gold
- SOCKS5: 218 alive / 114 gold

## Historical pool

- Discovered: 154713
- Ever alive: 28992
- Ever gold: 1118

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
