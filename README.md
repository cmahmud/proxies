# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 394
- HTTP: 81 alive / 57 gold
- HTTPS: 39 alive / 16 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 173 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36764
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
