# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 434
- HTTP: 130 alive / 78 gold
- HTTPS: 90 alive / 23 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34685
- Ever gold: 1257

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
