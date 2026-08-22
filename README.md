# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 414
- HTTP: 278 alive / 81 gold
- HTTPS: 190 alive / 30 gold
- SOCKS4: 206 alive / 137 gold
- SOCKS5: 244 alive / 166 gold

## Historical pool

- Discovered: 163879
- Ever alive: 32031
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
