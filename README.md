# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 398
- HTTP: 96 alive / 54 gold
- HTTPS: 55 alive / 18 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36826
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
