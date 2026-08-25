# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 406
- HTTP: 96 alive / 59 gold
- HTTPS: 78 alive / 20 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 175 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36911
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
