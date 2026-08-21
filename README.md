# SyndProxy private pool

## Current pool

- Alive now: 898
- Gold now: 397
- HTTP: 261 alive / 87 gold
- HTTPS: 171 alive / 22 gold
- SOCKS4: 223 alive / 142 gold
- SOCKS5: 243 alive / 146 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29722
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
