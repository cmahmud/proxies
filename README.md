# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 392
- HTTP: 81 alive / 55 gold
- HTTPS: 41 alive / 16 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 173 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36767
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
