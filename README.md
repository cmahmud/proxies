# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 429
- HTTP: 128 alive / 82 gold
- HTTPS: 141 alive / 19 gold
- SOCKS4: 187 alive / 161 gold
- SOCKS5: 197 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42200
- Ever gold: 1353

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
