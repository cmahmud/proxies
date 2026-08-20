# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 371
- HTTP: 185 alive / 75 gold
- HTTPS: 185 alive / 18 gold
- SOCKS4: 183 alive / 121 gold
- SOCKS5: 224 alive / 157 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26136
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
