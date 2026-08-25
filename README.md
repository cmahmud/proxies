# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 411
- HTTP: 98 alive / 63 gold
- HTTPS: 65 alive / 21 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36935
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
