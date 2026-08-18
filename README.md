# SyndProxy private pool

## Current pool

- Alive now: 874
- Gold now: 262
- HTTP: 230 alive / 32 gold
- HTTPS: 213 alive / 4 gold
- SOCKS4: 229 alive / 129 gold
- SOCKS5: 202 alive / 97 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10661
- Ever gold: 378

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
