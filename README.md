# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 397
- HTTP: 143 alive / 74 gold
- HTTPS: 178 alive / 24 gold
- SOCKS4: 167 alive / 147 gold
- SOCKS5: 178 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40060
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
