# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 470
- HTTP: 281 alive / 121 gold
- HTTPS: 215 alive / 86 gold
- SOCKS4: 187 alive / 123 gold
- SOCKS5: 225 alive / 140 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17496
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
