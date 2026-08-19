# SyndProxy private pool

## Current pool

- Alive now: 1255
- Gold now: 385
- HTTP: 428 alive / 90 gold
- HTTPS: 299 alive / 16 gold
- SOCKS4: 221 alive / 129 gold
- SOCKS5: 307 alive / 150 gold

## Historical pool

- Discovered: 134541
- Ever alive: 22004
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
