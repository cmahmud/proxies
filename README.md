# SyndProxy private pool

## Current pool

- Alive now: 675
- Gold now: 378
- HTTP: 176 alive / 64 gold
- HTTPS: 103 alive / 17 gold
- SOCKS4: 201 alive / 152 gold
- SOCKS5: 195 alive / 145 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25704
- Ever gold: 1072

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
