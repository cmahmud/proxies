# SyndProxy private pool

## Current pool

- Alive now: 1023
- Gold now: 423
- HTTP: 322 alive / 91 gold
- HTTPS: 235 alive / 25 gold
- SOCKS4: 236 alive / 156 gold
- SOCKS5: 230 alive / 151 gold

## Historical pool

- Discovered: 158244
- Ever alive: 30049
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
