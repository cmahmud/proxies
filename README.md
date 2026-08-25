# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 405
- HTTP: 92 alive / 63 gold
- HTTPS: 47 alive / 18 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36755
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
