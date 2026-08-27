# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 407
- HTTP: 86 alive / 64 gold
- HTTPS: 155 alive / 15 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41037
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
