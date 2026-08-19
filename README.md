# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 397
- HTTP: 331 alive / 73 gold
- HTTPS: 241 alive / 16 gold
- SOCKS4: 248 alive / 150 gold
- SOCKS5: 228 alive / 158 gold

## Historical pool

- Discovered: 129320
- Ever alive: 20491
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
