# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 404
- HTTP: 83 alive / 57 gold
- HTTPS: 54 alive / 17 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36593
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
