# SyndProxy private pool

## Current pool

- Alive now: 1130
- Gold now: 397
- HTTP: 400 alive / 111 gold
- HTTPS: 276 alive / 29 gold
- SOCKS4: 211 alive / 116 gold
- SOCKS5: 243 alive / 141 gold

## Historical pool

- Discovered: 160249
- Ever alive: 30675
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
