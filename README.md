# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 321
- HTTP: 281 alive / 34 gold
- HTTPS: 199 alive / 10 gold
- SOCKS4: 229 alive / 144 gold
- SOCKS5: 229 alive / 133 gold

## Historical pool

- Discovered: 106999
- Ever alive: 14207
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
