# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 406
- HTTP: 96 alive / 60 gold
- HTTPS: 66 alive / 18 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36859
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
