# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 393
- HTTP: 98 alive / 53 gold
- HTTPS: 43 alive / 16 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36774
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
