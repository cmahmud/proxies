# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 407
- HTTP: 255 alive / 82 gold
- HTTPS: 173 alive / 29 gold
- SOCKS4: 212 alive / 131 gold
- SOCKS5: 242 alive / 165 gold

## Historical pool

- Discovered: 162744
- Ever alive: 31502
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
