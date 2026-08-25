# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 411
- HTTP: 96 alive / 59 gold
- HTTPS: 43 alive / 19 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 194 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36707
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
