# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 396
- HTTP: 138 alive / 74 gold
- HTTPS: 175 alive / 24 gold
- SOCKS4: 164 alive / 147 gold
- SOCKS5: 174 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40068
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
