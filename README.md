# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 402
- HTTP: 81 alive / 54 gold
- HTTPS: 57 alive / 18 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36664
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
