# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 412
- HTTP: 100 alive / 61 gold
- HTTPS: 48 alive / 19 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36706
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
