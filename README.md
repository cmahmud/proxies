# SyndProxy validated proxy pool

## Current pool

- Alive now: 672
- Gold now: 480
- HTTP: 164 alive / 102 gold
- HTTPS: 117 alive / 39 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 213 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45254
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
