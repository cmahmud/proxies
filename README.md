# SyndProxy private pool

## Current pool

- Alive now: 1955
- Gold now: 656
- HTTP: 770 alive / 224 gold
- HTTPS: 624 alive / 123 gold
- SOCKS4: 244 alive / 145 gold
- SOCKS5: 317 alive / 164 gold

## Historical pool

- Discovered: 142699
- Ever alive: 24349
- Ever gold: 983

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
