# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 393
- HTTP: 279 alive / 78 gold
- HTTPS: 201 alive / 19 gold
- SOCKS4: 201 alive / 133 gold
- SOCKS5: 230 alive / 163 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29685
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
