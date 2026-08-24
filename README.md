# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 397
- HTTP: 126 alive / 63 gold
- HTTPS: 55 alive / 11 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 194 alive / 164 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33328
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
