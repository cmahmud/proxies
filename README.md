# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 392
- HTTP: 117 alive / 59 gold
- HTTPS: 74 alive / 16 gold
- SOCKS4: 173 alive / 155 gold
- SOCKS5: 188 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33522
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
