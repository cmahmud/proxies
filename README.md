# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 416
- HTTP: 104 alive / 68 gold
- HTTPS: 48 alive / 18 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36736
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
