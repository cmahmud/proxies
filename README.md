# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 339
- HTTP: 111 alive / 38 gold
- HTTPS: 62 alive / 7 gold
- SOCKS4: 173 alive / 154 gold
- SOCKS5: 188 alive / 140 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32892
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
