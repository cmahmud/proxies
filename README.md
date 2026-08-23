# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 391
- HTTP: 113 alive / 63 gold
- HTTPS: 58 alive / 15 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 190 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33171
- Ever gold: 1229

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
