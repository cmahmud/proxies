# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 393
- HTTP: 78 alive / 50 gold
- HTTPS: 45 alive / 13 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36558
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
