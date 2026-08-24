# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 389
- HTTP: 89 alive / 52 gold
- HTTPS: 40 alive / 13 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 194 alive / 164 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33344
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
