# SyndProxy private pool

## Current pool

- Alive now: 1857
- Gold now: 654
- HTTP: 722 alive / 235 gold
- HTTPS: 616 alive / 116 gold
- SOCKS4: 222 alive / 145 gold
- SOCKS5: 297 alive / 158 gold

## Historical pool

- Discovered: 142693
- Ever alive: 24287
- Ever gold: 981

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
