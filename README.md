# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 421
- HTTP: 88 alive / 63 gold
- HTTPS: 70 alive / 22 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 192 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36107
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
