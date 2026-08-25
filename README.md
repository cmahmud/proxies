# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 407
- HTTP: 84 alive / 63 gold
- HTTPS: 42 alive / 17 gold
- SOCKS4: 166 alive / 164 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36753
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
