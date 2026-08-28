# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 406
- HTTP: 85 alive / 64 gold
- HTTPS: 86 alive / 17 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 184 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42702
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
