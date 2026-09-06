# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 396
- HTTP: 115 alive / 74 gold
- HTTPS: 64 alive / 18 gold
- SOCKS4: 172 alive / 151 gold
- SOCKS5: 183 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48073
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
