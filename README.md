# SyndProxy private pool

## Current pool

- Alive now: 876
- Gold now: 414
- HTTP: 251 alive / 82 gold
- HTTPS: 182 alive / 30 gold
- SOCKS4: 201 alive / 137 gold
- SOCKS5: 242 alive / 165 gold

## Historical pool

- Discovered: 163879
- Ever alive: 32032
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
