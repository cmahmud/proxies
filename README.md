# SyndProxy private pool

## Current pool

- Alive now: 1137
- Gold now: 566
- HTTP: 428 alive / 173 gold
- HTTPS: 295 alive / 117 gold
- SOCKS4: 207 alive / 133 gold
- SOCKS5: 207 alive / 143 gold

## Historical pool

- Discovered: 127345
- Ever alive: 19829
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
