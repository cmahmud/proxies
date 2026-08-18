# SyndProxy private pool

## Current pool

- Alive now: 658
- Gold now: 240
- HTTP: 204 alive / 29 gold
- HTTPS: 93 alive / 5 gold
- SOCKS4: 171 alive / 113 gold
- SOCKS5: 190 alive / 93 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10280
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
