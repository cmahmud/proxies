# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 412
- HTTP: 87 alive / 60 gold
- HTTPS: 70 alive / 18 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36314
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
