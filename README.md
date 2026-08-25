# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 401
- HTTP: 91 alive / 59 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36778
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
