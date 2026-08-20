# SyndProxy private pool

## Current pool

- Alive now: 1372
- Gold now: 567
- HTTP: 551 alive / 180 gold
- HTTPS: 368 alive / 90 gold
- SOCKS4: 212 alive / 134 gold
- SOCKS5: 241 alive / 163 gold

## Historical pool

- Discovered: 138835
- Ever alive: 23075
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
