# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 395
- HTTP: 110 alive / 73 gold
- HTTPS: 49 alive / 16 gold
- SOCKS4: 167 alive / 151 gold
- SOCKS5: 184 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48100
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
