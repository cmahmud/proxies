# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 394
- HTTP: 114 alive / 59 gold
- HTTPS: 73 alive / 15 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33522
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
