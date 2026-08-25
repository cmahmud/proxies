# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 400
- HTTP: 92 alive / 59 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36778
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
