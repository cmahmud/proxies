# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 410
- HTTP: 102 alive / 59 gold
- HTTPS: 46 alive / 19 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36706
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
