# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 415
- HTTP: 85 alive / 64 gold
- HTTPS: 45 alive / 20 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48856
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
