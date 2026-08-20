# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 397
- HTTP: 349 alive / 73 gold
- HTTPS: 196 alive / 20 gold
- SOCKS4: 211 alive / 154 gold
- SOCKS5: 229 alive / 150 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26792
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
