# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 413
- HTTP: 113 alive / 64 gold
- HTTPS: 154 alive / 18 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41257
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
