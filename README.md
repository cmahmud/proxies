# SyndProxy validated proxy pool

## Current pool

- Alive now: 456
- Gold now: 393
- HTTP: 78 alive / 56 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 173 alive / 163 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36767
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
