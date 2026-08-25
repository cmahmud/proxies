# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 406
- HTTP: 95 alive / 58 gold
- HTTPS: 77 alive / 20 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 175 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36912
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
