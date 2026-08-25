# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 410
- HTTP: 99 alive / 64 gold
- HTTPS: 94 alive / 20 gold
- SOCKS4: 179 alive / 158 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35464
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
