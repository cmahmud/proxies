# SyndProxy private pool

## Current pool

- Alive now: 862
- Gold now: 391
- HTTP: 274 alive / 81 gold
- HTTPS: 163 alive / 23 gold
- SOCKS4: 189 alive / 129 gold
- SOCKS5: 236 alive / 158 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29687
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
