# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 402
- HTTP: 86 alive / 55 gold
- HTTPS: 57 alive / 18 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36688
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
