# SyndProxy private pool

## Current pool

- Alive now: 646
- Gold now: 382
- HTTP: 157 alive / 66 gold
- HTTPS: 93 alive / 16 gold
- SOCKS4: 195 alive / 146 gold
- SOCKS5: 201 alive / 154 gold

## Historical pool

- Discovered: 146602
- Ever alive: 25690
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
