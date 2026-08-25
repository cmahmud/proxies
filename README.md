# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 407
- HTTP: 86 alive / 64 gold
- HTTPS: 42 alive / 17 gold
- SOCKS4: 167 alive / 164 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36753
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
