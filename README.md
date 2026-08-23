# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 390
- HTTP: 104 alive / 62 gold
- HTTPS: 53 alive / 15 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 187 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33169
- Ever gold: 1229

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
