# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 392
- HTTP: 105 alive / 70 gold
- HTTPS: 46 alive / 14 gold
- SOCKS4: 167 alive / 153 gold
- SOCKS5: 184 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48102
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
