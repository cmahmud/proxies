# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 400
- HTTP: 86 alive / 57 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36646
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
