# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 411
- HTTP: 85 alive / 64 gold
- HTTPS: 65 alive / 17 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36377
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
