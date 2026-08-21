# SyndProxy private pool

## Current pool

- Alive now: 841
- Gold now: 366
- HTTP: 218 alive / 75 gold
- HTTPS: 190 alive / 23 gold
- SOCKS4: 196 alive / 133 gold
- SOCKS5: 237 alive / 135 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29656
- Ever gold: 1134

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
