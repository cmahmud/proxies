# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 396
- HTTP: 111 alive / 74 gold
- HTTPS: 63 alive / 18 gold
- SOCKS4: 173 alive / 151 gold
- SOCKS5: 184 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48073
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
