# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 417
- HTTP: 93 alive / 65 gold
- HTTPS: 64 alive / 23 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36941
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
