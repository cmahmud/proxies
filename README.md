# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 398
- HTTP: 91 alive / 55 gold
- HTTPS: 51 alive / 12 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36606
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
