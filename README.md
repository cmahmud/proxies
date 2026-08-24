# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 397
- HTTP: 122 alive / 62 gold
- HTTPS: 44 alive / 13 gold
- SOCKS4: 173 alive / 155 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33665
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
