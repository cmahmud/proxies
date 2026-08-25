# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 410
- HTTP: 86 alive / 62 gold
- HTTPS: 57 alive / 16 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36329
- Ever gold: 1272

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
