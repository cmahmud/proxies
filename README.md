# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 411
- HTTP: 91 alive / 62 gold
- HTTPS: 61 alive / 21 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36900
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
