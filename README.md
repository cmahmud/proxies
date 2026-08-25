# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 413
- HTTP: 88 alive / 59 gold
- HTTPS: 65 alive / 18 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36285
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
