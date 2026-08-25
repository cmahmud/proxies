# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 398
- HTTP: 80 alive / 52 gold
- HTTPS: 51 alive / 17 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36579
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
