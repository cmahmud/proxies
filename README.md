# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 422
- HTTP: 97 alive / 72 gold
- HTTPS: 47 alive / 22 gold
- SOCKS4: 184 alive / 165 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49033
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
