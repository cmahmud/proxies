# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 397
- HTTP: 79 alive / 51 gold
- HTTPS: 49 alive / 16 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36568
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
