# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 383
- HTTP: 274 alive / 74 gold
- HTTPS: 134 alive / 20 gold
- SOCKS4: 192 alive / 128 gold
- SOCKS5: 244 alive / 161 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29697
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
