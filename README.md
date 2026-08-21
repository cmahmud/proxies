# SyndProxy private pool

## Current pool

- Alive now: 862
- Gold now: 368
- HTTP: 225 alive / 76 gold
- HTTPS: 197 alive / 23 gold
- SOCKS4: 198 alive / 133 gold
- SOCKS5: 242 alive / 136 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29656
- Ever gold: 1134

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
