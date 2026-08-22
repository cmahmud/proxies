# SyndProxy private pool

## Current pool

- Alive now: 828
- Gold now: 414
- HTTP: 230 alive / 92 gold
- HTTPS: 151 alive / 30 gold
- SOCKS4: 215 alive / 130 gold
- SOCKS5: 232 alive / 162 gold

## Historical pool

- Discovered: 163856
- Ever alive: 31951
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
