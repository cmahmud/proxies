# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 389
- HTTP: 81 alive / 54 gold
- HTTPS: 38 alive / 15 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36763
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
