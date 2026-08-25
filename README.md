# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 404
- HTTP: 88 alive / 60 gold
- HTTPS: 56 alive / 17 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36871
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
