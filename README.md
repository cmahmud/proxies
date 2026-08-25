# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 413
- HTTP: 93 alive / 61 gold
- HTTPS: 47 alive / 20 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36719
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
