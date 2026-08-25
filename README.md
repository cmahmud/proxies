# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 409
- HTTP: 99 alive / 61 gold
- HTTPS: 76 alive / 19 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36890
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
