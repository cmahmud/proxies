# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 416
- HTTP: 91 alive / 63 gold
- HTTPS: 52 alive / 20 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 181 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36746
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
