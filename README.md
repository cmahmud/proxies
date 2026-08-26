# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 413
- HTTP: 96 alive / 69 gold
- HTTPS: 78 alive / 19 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38651
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
