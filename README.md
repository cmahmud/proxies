# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 375
- HTTP: 82 alive / 46 gold
- HTTPS: 43 alive / 12 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 172315
- Ever alive: 32970
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
