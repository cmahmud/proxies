# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 413
- HTTP: 84 alive / 57 gold
- HTTPS: 50 alive / 18 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 192 alive / 175 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36286
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
