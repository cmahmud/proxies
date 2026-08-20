# SyndProxy private pool

## Current pool

- Alive now: 698
- Gold now: 360
- HTTP: 175 alive / 66 gold
- HTTPS: 148 alive / 18 gold
- SOCKS4: 188 alive / 133 gold
- SOCKS5: 187 alive / 143 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26660
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
