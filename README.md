# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 406
- HTTP: 85 alive / 63 gold
- HTTPS: 37 alive / 18 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36753
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
