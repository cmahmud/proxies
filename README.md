# SyndProxy private pool

## Current pool

- Alive now: 664
- Gold now: 202
- HTTP: 147 alive / 23 gold
- HTTPS: 115 alive / 9 gold
- SOCKS4: 192 alive / 89 gold
- SOCKS5: 210 alive / 81 gold

## Historical pool

- Discovered: 89658
- Ever alive: 7999
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
