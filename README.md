# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 395
- HTTP: 116 alive / 60 gold
- HTTPS: 78 alive / 15 gold
- SOCKS4: 173 alive / 156 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33522
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
