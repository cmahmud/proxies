# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 415
- HTTP: 89 alive / 65 gold
- HTTPS: 50 alive / 18 gold
- SOCKS4: 185 alive / 161 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48883
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
