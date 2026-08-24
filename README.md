# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 397
- HTTP: 154 alive / 64 gold
- HTTPS: 53 alive / 12 gold
- SOCKS4: 193 alive / 159 gold
- SOCKS5: 218 alive / 162 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33339
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
