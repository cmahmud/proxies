# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 525
- HTTP: 378 alive / 150 gold
- HTTPS: 274 alive / 89 gold
- SOCKS4: 225 alive / 149 gold
- SOCKS5: 206 alive / 137 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17731
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
