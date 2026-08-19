# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 528
- HTTP: 370 alive / 172 gold
- HTTPS: 243 alive / 92 gold
- SOCKS4: 202 alive / 129 gold
- SOCKS5: 214 alive / 135 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18782
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
