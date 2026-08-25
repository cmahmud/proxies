# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 410
- HTTP: 85 alive / 63 gold
- HTTPS: 64 alive / 17 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 194 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36376
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
