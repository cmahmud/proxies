# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 402
- HTTP: 133 alive / 70 gold
- HTTPS: 51 alive / 13 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 180 alive / 162 gold

## Historical pool

- Discovered: 177314
- Ever alive: 33278
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
