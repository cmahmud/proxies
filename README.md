# SyndProxy private pool

## Current pool

- Alive now: 1146
- Gold now: 556
- HTTP: 380 alive / 172 gold
- HTTPS: 330 alive / 84 gold
- SOCKS4: 221 alive / 151 gold
- SOCKS5: 215 alive / 149 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19759
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
