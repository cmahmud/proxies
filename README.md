# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 415
- HTTP: 92 alive / 66 gold
- HTTPS: 38 alive / 18 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36738
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
