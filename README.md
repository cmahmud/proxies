# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 415
- HTTP: 108 alive / 77 gold
- HTTPS: 45 alive / 19 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 184 alive / 160 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49460
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
