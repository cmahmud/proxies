# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 398
- HTTP: 74 alive / 54 gold
- HTTPS: 44 alive / 14 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36491
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
