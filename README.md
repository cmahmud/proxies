# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 409
- HTTP: 94 alive / 62 gold
- HTTPS: 45 alive / 19 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36746
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
