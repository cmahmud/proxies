# SyndProxy private pool

## Current pool

- Alive now: 628
- Gold now: 219
- HTTP: 146 alive / 24 gold
- HTTPS: 81 alive / 8 gold
- SOCKS4: 188 alive / 103 gold
- SOCKS5: 213 alive / 84 gold

## Historical pool

- Discovered: 91002
- Ever alive: 8003
- Ever gold: 346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
