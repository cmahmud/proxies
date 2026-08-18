# SyndProxy private pool

## Current pool

- Alive now: 695
- Gold now: 239
- HTTP: 179 alive / 31 gold
- HTTPS: 103 alive / 8 gold
- SOCKS4: 224 alive / 111 gold
- SOCKS5: 189 alive / 89 gold

## Historical pool

- Discovered: 86714
- Ever alive: 6881
- Ever gold: 323

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
