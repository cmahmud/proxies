# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 428
- HTTP: 110 alive / 70 gold
- HTTPS: 70 alive / 30 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 174 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47055
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
